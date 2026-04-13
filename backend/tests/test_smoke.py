from fastapi.testclient import TestClient
from sqlmodel import Session

from backend.models import UserSession


def test_root(client: TestClient):
    assert client.get("/").status_code == 200



