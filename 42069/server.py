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
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
YEAR = 365 * DAY

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
app.include_router(temp_capstone.router)
app.include_router(gsheet.router)
app.include_router(doto.router)


app.state.counter = 0
watcher = Watcher()
app.state.watcher = watcher.init_state


@app.get("/update-watcher-state")
def update_watcher_state():
    app.state.watcher = watcher.get_new_state(app.state.watcher)
    return app.state.watcher


@app.on_event("startup")
@repeat_every(seconds=1)
@app.get("/debug-repeater")
def repeater():
    try:
        if not app.state.counter % MINUTE:
            update_watcher_state()
        if not app.state.counter % HOUR:
            doto.get_new_state()
        if not app.state.counter % YEAR:
            app.state.counter = 0
        app.state.counter += 1
    except Exception as e:
        return {"error": str(e)}
    return app.state.counter


