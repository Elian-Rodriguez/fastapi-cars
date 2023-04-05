from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
import os
from dotenv import load_dotenv
from supabase import create_client, Client
load_dotenv()

user_router = APIRouter()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

@user_router.post('/register', tags=['auth'])
async def  register(user: User):
    print(f"{user}")
    res = supabase.auth.sign_up({
        "email": user.email,
        "password": user.password,
    })
    #print(f"--------------- {type(res)}    ---------- {res}")
    return JSONResponse(status_code=200, content={"mesages":"Por favor falidar su correo electronico para confirmar login"})
    

@user_router.post('/login', tags=['auth'])
async def login(user: User):
    """
       Se requiere autenticación JWT para acceder a esta ruta. El usuario para la autenticación es admin@gmail.com con contraseña admin.
    """
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


    # Registro con Supabase

    auth_resp = supabase.auth.sign_in_with_password({"email": user.email, "password": user.password})
    token = auth_resp.session.access_token
    
    #token: str = create_token(auth_resp['user'])
    return JSONResponse(status_code=200, content=token)