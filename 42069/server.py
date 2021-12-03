from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from starlette.middleware.cors import CORSMiddleware


from internal.watcher import Watcher
from utils.util_func import load_env

# Initializing services
from routers import (
    lai,
    twither,
    gprocurement,
    temp_capstone,
    gsheet,
    doto
)

load_env('.env')
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
app.include_router(doto.router)

watcher = Watcher()
app.state.watcher = watcher.init_state
app.state.doto = doto.init_state()


@app.get("/update-watcher-state")
async def update_watcher_state():
    app.state.watcher = watcher.get_new_state(app.state.watcher)
    return app.state.watcher


@app.on_event("startup")
@repeat_every(seconds=60 * 60)
async def repeater():
    await update_watcher_state()
    app.state.doto = await doto.get_new_state(app.state.doto)
