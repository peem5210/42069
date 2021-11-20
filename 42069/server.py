from fastapi import FastAPI
from utils.util_func import load_env
from routers import (
    lai,
    twither,
    )

load_env()
app = FastAPI()

app.include_router(lai.router)
app.include_router(twither.router)
