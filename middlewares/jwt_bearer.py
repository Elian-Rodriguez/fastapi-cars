from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import create_token, validate_token
import os
from dotenv import load_dotenv
from supabase import create_client, Client


supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        print(f"{data}")
        print(f"{data['email'] }")
        if  data['email'] == None:
            raise HTTPException(status_code=403, detail="Credenciales son invalidas")
