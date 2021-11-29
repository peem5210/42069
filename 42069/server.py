from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from utils.util_func import load_env
from routers import (
    lai,
    twither,
    gprocurement
    )

load_env()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(lai.router)
app.include_router(twither.router)
app.include_router(gprocurement.router)
