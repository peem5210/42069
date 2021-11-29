from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import (
    lai,
    twither,
    gprocurement,
    temp_capstone
    )


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
app.include_router(temp_capstone.router)

