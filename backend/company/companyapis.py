from fastapi import APIRouter, Depends

from .dependencies import get_token_header

router = APIRouter(
    prefix="/companyapis",
    tags=["companysapis"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)


@router.get("/")
async def get_company_name():
    return {"company_name": "Example Company, LLC"}


@router.get("/employees")
async def number_of_employees():
    return 162
