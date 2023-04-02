from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.car import cars_router
from routers.user import user_router
from utils.cars import load_data_cars
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()

app.title = "Autos Deportivos con  FastAPI"
app.version = "0.0.1"


app.add_middleware(ErrorHandler)

app.include_router(cars_router)
app.include_router(user_router)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

load_data_cars()


def my_task():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    load_data_cars()
    
# Decorar la función con @background_task
@app.post("/automatic-task" , tags=['jobs'])
async def ejecutar_tarea(background_tasks: BackgroundTasks):
    """
    Ejecuta una tarea automática que actualiza la base de datos de coches con los datos por defecto
    Esta se ejecuta cada 30 minutos dejando en base de datos 13 vehiculos en lista
    """
    background_tasks.add_task(my_task)
    
    

@app.get('/', tags=['ping'])
def message():
    return HTMLResponse('<h1>I am alive<h1>')


# Crear un objeto Scheduler y configurarlo para que ejecute la tarea cada 30 minutos
scheduler = BackgroundScheduler()
scheduler.add_job(func=my_task, trigger='cron', minute='*/30')

# Iniciar el planificador
scheduler.start()

"""  python -m uvicorn main:app --reload"""
