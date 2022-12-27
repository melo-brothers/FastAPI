from fastapi import status
from fastapi.testclient import TestClient


def test_get_todos_by_user(client: TestClient):
    resp = client.get("/todos/user")
    assert resp.status_code == status.HTTP_200_OK


def test_get_todos_by_user_returns_empty_list(client: TestClient):
    resp = client.get("/todos/user")
    assert resp.json() == []
