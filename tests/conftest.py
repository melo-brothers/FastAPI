import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.auth.services import get_current_user
from backend.core.database import Base, get_db
from backend.main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, poolclass=StaticPool, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def override_user():
    return {"username": "admin", "id": 1}


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_user


@pytest.fixture
def client():
    try:
        Base.metadata.create_all(bind=engine)
        with TestClient(app) as t:
            yield t
    finally:
        Base.metadata.drop_all(bind=engine)
