from fastapi import FastAPI
from fastapi.exception_handlers import (
    http_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from .routers import router

origins = [
    'http://localhost'
]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=['*'],
    )
]

app = FastAPI(middleware=middleware)
app.include_router(router)


@app.exception_handler(StarletteHTTPException)
async def exception_handler(request, exc):
    print(f"Exception: {repr(exc)}")
    return await http_exception_handler(request, exc)
