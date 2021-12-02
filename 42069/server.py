from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from starlette.middleware.cors import CORSMiddleware
from internal.watcher import init_state, Watcher

from routers import (
    lai,
    twither,
    gprocurement,
    temp_capstone,
    gsheet
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
app.include_router(gsheet.router)

app.state.watcher = init_state()
watcher = Watcher()


@app.get("/")
async def update_watcher_state():
    app.state.watcher = watcher.get_new_state(app.state.watcher)
    return app.state.watcher


@app.on_event("startup")
@repeat_every(seconds=1000)
async def repeater():
    app.state.watcher = watcher.get_new_state(app.state.watcher)
