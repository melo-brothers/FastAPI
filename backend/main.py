from fastapi import FastAPI

from .addresses import address
from .auth.routes import router as auth_router
from .company import companyapis
from .settings import DEBUG
from .todos.routes import router as todo_router

app = FastAPI(debug=DEBUG)

app.include_router(auth_router)
app.include_router(todo_router)
app.include_router(address.router)
app.include_router(companyapis.router)
