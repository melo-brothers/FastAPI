from fastapi import Depends, FastAPI

from . import models
from .company import companyapis, dependencies
from .routers import address, auth, todos

app = FastAPI()

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(
    companyapis.router,
    prefix="/companyapis",
    tags=["companysapis"],
    dependencies=[Depends(dependencies.get_token_header)],
    responses={418: {"description": "Internal Use Only"}}
)
