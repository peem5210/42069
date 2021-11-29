from fastapi import APIRouter
from services.gprocurement.gprocurement_service import GprocurementService

router = APIRouter(
    prefix="/gprocurement",
    tags=["gprocurement"],
    responses={404: {"description": "Not found, Sucker "}},
)
gprocurement_service = GprocurementService()


@router.get("/e-bidding/")
async def ebidding(
        page: int = 0,
        project_type: str = '01',
        sdate: str = '',
        edate: str = '',
        budget: int = 0,
        project_id: str = '',
        dept_id: str = ''
):
    return gprocurement_service.get_ebidding(page, project_type, sdate, edate, budget, project_id, dept_id)
