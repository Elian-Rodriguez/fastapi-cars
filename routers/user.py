from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User):
    """
       Se requiere autenticación JWT para acceder a esta ruta. El usuario para la autenticación es admin@gmail.com con contraseña admin.
    """
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)