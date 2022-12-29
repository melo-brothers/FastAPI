from fastapi import APIRouter

from ..core.errors import ERROR_MESSAGES

router = APIRouter(
    tags=["observability"],
    responses={404: {"description": "Not found"}}
)


@router.get("/health")
async def health():
    return "UP!"


@router.get("/errors")
async def all_errors():
    return ERROR_MESSAGES


@router.get("/errors/{msg_code}")
async def error_detail(msg_code: int):
    return ERROR_MESSAGES[msg_code]
