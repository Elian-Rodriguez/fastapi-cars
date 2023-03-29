from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from models.car import SportsCar as SportCarModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.car import SportsCarService
from schemas.car import SportsCar

cars_router = APIRouter()


@cars_router.get('/sportcars', tags=['cars'], response_model=List[SportsCar], status_code=200, dependencies=[Depends(JWTBearer())])
def get_cars() -> List[SportsCar]:
    db = Session()
    result = SportsCarService(db).get_cars
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@cars_router.get('/sportcars/{id}', tags=['cars'], response_model=SportsCar)
def get_car(id: int = Path(ge=1, le=2000)) -> SportsCar:
    db = Session()
    result = SportsCarService(db).get_car(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@cars_router.get('/sportcars/', tags=['cars'], response_model=List[SportsCar])
def get_cars_by_year(year: int = Query(ge=1900, le=2022)) -> List[SportsCar]:
    db = Session()
    result = SportsCarService(db).get_cars_by_category(year)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@cars_router.post('/sportcars', tags=['cars'], response_model=dict, status_code=201)
def create_car(cars: SportsCar) -> dict:
    db = Session()
    SportsCarService(db).create_car(cars)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el Vehiculo"})


@cars_router.put('/sportcars/{id}', tags=['cars'], response_model=dict, status_code=200)
def update_movie(id: int, car: SportsCar)-> dict:
    db = Session()
    result = SportsCarService(db).get_car(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
    SportsCarService(db).update_car(id, car)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado El vehiculo"})


@cars_router.delete('/sportcars/{id}', tags=['cars'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = Session()
    result: SportCarModel = db.query(SportCarModel).filter(SportCarModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    SportsCarService(db).delete_car(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado El vehiculo"})