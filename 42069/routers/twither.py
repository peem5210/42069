from typing import Union
from fastapi import APIRouter
from services.twither.twither_service import TwitherService

router = APIRouter(
    prefix="/twitter",
    tags=["twitter"],
    responses={404: {"description": "Sucker"}},
)
twither_service = TwitherService()


@router.get("/")
async def twitter():
    return [{"msg": f"kk"}, {"test": "test"}]


@router.get("/{msg}")
async def twitter(msg: str):
    res: dict[str, Union[str, int]] = twither_service.do_something()
    return {"msg": msg, "status": res['status']}
