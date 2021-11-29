from fastapi import APIRouter
from services.temp.capstone.capstone_service import CapStoneService

router = APIRouter(
    prefix="/capstone",
    tags=["capstone"],
    responses={404: {"description": "Not found, Sucker "}},
)
capstone_service = CapStoneService()


@router.post("/store-json/")
async def store_json(json: dict):
    return capstone_service.open_and_store_json(json)

@router.post("/store-json/{name}")
async def store_json(json: dict, name:str):
    return capstone_service.open_and_store_json(json, name=name)

@router.get("/read-all-json/")
async def read_all():
    return capstone_service.read_all()


@router.get("/clear/")
async def clear():
    return capstone_service.clear()
