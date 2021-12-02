from typing import Union
from fastapi import APIRouter
from services.lai.lai_service import LaiService
from utils.util_func import load_env

router = APIRouter(
    prefix="/line",
    tags=["line"],
    responses={404: {"description": "Not found, Sucker "}},
)
load_env("./configs/lai.env")
lai_service = LaiService()
lai_service.send_msg("Starting lai service...", force=False)


@router.get("/")
async def line(msg: str):
    res: dict[str, Union[str, int]] = lai_service.send_msg(msg)
    return {"msg": msg, "status": res['status']}


@router.get("/{msg}")
async def line(msg: str):
    res: dict[str, Union[str, int]] = lai_service.send_msg(msg)
    return {"msg": msg, "status": res['status']}
