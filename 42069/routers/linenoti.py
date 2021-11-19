from typing import Union
from fastapi import APIRouter
from service.linenoti.linenoti_service import LineNotiService

router = APIRouter(
    prefix="/line",
    tags=["line"],
    responses={404: {"description": "Fuck you"}},
)
linenoti_service = LineNotiService()


@router.get("/")
async def line():
    return [{"msg": f"kk"}, {"test": "Morty"}]


@router.get("/{msg}")
async def line(msg: str):
    res: dict[str, Union[str, int]] = linenoti_service.send_msg(msg)
    return {"msg": msg, "status": res['status']}
