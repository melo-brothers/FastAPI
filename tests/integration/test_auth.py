from fastapi import status
from fastapi.testclient import TestClient

BODY = {
    "username": "admin",
    "email": "admin@admin.com",
    "first_name": "super",
    "last_name": "admin",
    "password": "admin"
}

def test_create_user_must_return_user_info(client: TestClient):
    resp = client.post("/auth/create/user", json=BODY)
    assert resp.json() == {'email': 'admin@admin.com', 'id': 1, 'username': 'admin'}


def test_create_user_must_return_status_code_201(client: TestClient):
    resp = client.post("/auth/create/user", json=BODY)
    assert resp.status_code == status.HTTP_201_CREATED


def test_get_valid_token(client: TestClient):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "username": BODY["username"],
        "password": BODY["password"],
    }
    client.post("/auth/create/user", json=BODY)
    resp = client.post("/auth/token", headers=headers, data=payload)
    assert resp.json()["token"] is not None


def test_invalid_token_must_raises_unauthorized(client: TestClient):
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {
        "username": BODY["username"],
        "password": "senhaInvalida",
    }
    client.post("/auth/create/user", json=BODY)
    resp = client.post("/auth/token", headers=headers, data=payload)
    assert resp.status_code == status.HTTP_401_UNAUTHORIZED
