from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                return JSONResponse(status_code=400, content={'error': 'Valor del Id duplicado'})
            return JSONResponse(status_code=500, content={'error': 'Error en la base de datos'})
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
