from typing import Union
from fastapi import APIRouter
from services.lai.lai_service import LaiService

router = APIRouter(
    prefix="/line",
    tags=["line"],
    responses={404: {"description": "Not found, Sucker "}},
)
lai_service = LaiService()


@router.get("/")
async def line(msg: str):
    res: dict[str, Union[str, int]] = lai_service.send_msg(msg)
    return {"msg": msg, "status": res['status']}


@router.get("/{msg}")
async def line(msg: str):
    res: dict[str, Union[str, int]] = lai_service.send_msg(msg)
    return {"msg": msg, "status": res['status']}
