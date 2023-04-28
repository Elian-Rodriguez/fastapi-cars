# FASTAPI CARS
El proyecto utiliza el marco de trabajo FastAPI para la creación de servicios web. Para la base de datos, utiliza SQLAlchemy, una biblioteca de Python para trabajar con bases de datos SQL. Utiliza apscheduler para programar tareas y se ejecuta en un intervalo de 30 minutos. También utiliza Supabase para la autenticación de usuarios y generación de tokens JWT

El objetivo del proyecto es crear una API RESTful que permita a los clientes realizar operaciones CRUD (Create, Read, Update, Delete) en la base de datos de sports_cars. Para ello, se utiliza el framework FastAPI para implementar la API, que se ejecuta dentro de un contenedor Docker para garantizar la portabilidad y la escalabilidad del servicio.

Además, para permitir la comunicación en tiempo real con los clientes, se utiliza la plataforma de mensajería Fli.io, que proporciona una API para enviar y recibir mensajes de forma eficiente.

## Instalacion de Requerimientos
1. Creacion del entorno vitutal
```bash
python -m venv nombre_entorno
```
2. Activacion del entorno virtual
```bash
source nombre_entorno/bin/activate
```

## Instalacion de Requerimientos
```bash
pip install -r requirements.txt
```
## Descripcion de las variables de entorno
Antes de iniciar con la configuración del API, es necesario contar con las siguientes variables de entorno configuradas:

- SUPABASE_URL: URL de la instancia de Supabase que se utilizará para almacenar los datos del API.
- SUPABASE_KEY: Llave de acceso para la instancia de Supabase.
- JWT_SECRET: Llave secreta para la generación de tokens JWT.
- JWT_ALGORITHM: Algoritmo de encriptación utilizado para generar los tokens JWT.

Se usa Supabase para generacion de JWT y almacenado y registro de los usuarios.

## Ejecucion de la api
```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```
