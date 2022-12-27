from fastapi import FastAPI

from .company import companyapis
from .routers import address, auth, todos

app = FastAPI()

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)
app.include_router(companyapis.router)
