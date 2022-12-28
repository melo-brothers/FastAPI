from fastapi import APIRouter

from ..core.errors import error_messages

router = APIRouter(
    tags=["observability"],
    responses={404: {"description": "Not found"}}
)


@router.get("/health")
async def health():
    return "UP!"


@router.get("/errors")
async def all_errors():
    return error_messages


@router.get("/errors/{msg_code}")
async def error_detail(msg_code: int):
    return error_messages[msg_code]
