from typing import Union
from fastapi import APIRouter

from services.doto.doto_service import DotoService
from services.lai.lai_service import LaiService
from utils.util_func import load_env

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found, Sucker "}},
)
load_env("./configs/lai.env")
doto_service = DotoService()
lai_service = LaiService()


@router.get("/")
async def get_todos():
    res: dict[str, Union[str, int]] = doto_service.get_todos()
    return res


@router.get("/add/{todo}/{desc}/{priority}")
async def add_todo(todo: str, desc: str, priority: str):
    res: dict[str, Union[str, int]] = doto_service.add_todo(todo, desc, priority)
    return res


@router.get("/add/{todo}/{desc}/")
async def add_todo(todo: str, desc: str):
    res: dict[str, Union[str, int]] = doto_service.add_todo(todo, desc, '-')
    return res


@router.get("/add/{todo}/")
async def add_todo(todo: str):
    res: dict[str, Union[str, int]] = doto_service.add_todo(todo, '-', '-')
    return res


@router.get("/complete/{id}")
async def get_todo(id):
    res = doto_service.complete_todo(id)
    return res


@router.get("/notify")
async def get_new_state(state):
    doto_df = doto_service.get_todos(json=False)
    doto_df = doto_df[(doto_df.MUTE == '') & (doto_df.COMPLETION != "Yes")]
    doto_df['msg'] = doto_df.ID + ': ' + doto_df.TODO
    todos = doto_df.msg.values.tolist()
    if len(todos) > 0:
        msg = 'TODOs ::\n' + ('\n'.join(todos))
        lai_service.send_msg(msg)
        state['count'] += 1
        return state


def init_state():
    return {
        'count': 0
    }
