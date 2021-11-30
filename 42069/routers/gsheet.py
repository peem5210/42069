from fastapi import APIRouter
from services.gsheet.gsheet_service import GSheetService
from utils.util_func import load_env

router = APIRouter(
    prefix="/gsheet",
    tags=["gsheet"],
    responses={404: {"description": "Not found, Sucker "}},
)
load_env(path='./configs/google_sheet.env')
service = GSheetService()


@router.get("/")
async def sheet_list():
    res = service.sheet_list()
    return res


@router.get("/{sheet_name}/{cell}")
async def get_cell(sheet_name: str, cell: str):
    res = service.get_cell(sheet_name, cell)
    return res
