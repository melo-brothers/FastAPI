from fastapi import FastAPI

from . import __version__
from .addresses import address
from .auth.routes import router as auth_router
from .company import companyapis
from .observability.routes import router as observability_router
from .settings import DEBUG
from .todos.routes import router as todo_router


app_info = {
    "debug": DEBUG,
    "version": __version__,
    "description": ("A Backend API is an Application Programming Interface " "that developers can use to integrate with backend services."),
}


app = FastAPI(**app_info)
route = app.include_router

route(auth_router)
route(todo_router)
route(address.router)
route(companyapis.router)
route(observability_router)
