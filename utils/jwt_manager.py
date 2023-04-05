from jwt import encode, decode
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from typing import Dict
import time
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

"""def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data"""


def validate_token(token: str) -> dict:
    try:
        # Decodificar el token
        data = supabase.auth.get_user(token)
        #print(f"-------------data---{type(data)}---------------------------{data}")
        email = data.user.email
        #print(f"-------------email---{type(email)}---------------------------{email}")
        payload = {'email':email,'message':'Tokent Valido'}

        # Retornar el correo electrónico del usuario que generó el token
        return payload
    except jwt.ExpiredSignatureError:
        # Si el token ha expirado
        return {'email':None,'message':'Tokent expirado'}

    except jwt.InvalidTokenError as e:
        # Si el token es inválido
        return {'email':None,'message':f'Tokent invalido {str(e)}'}

    
    