from fastapi import FastAPI
from util.util_func import load_env
from routers import (
    linenoti,
    )
load_env()
app = FastAPI()


app.include_router(linenoti.router)
