from fastapi.testclient import TestClient
from sqlmodel import Session

from backend.app import app
from backend.database import engine
from backend.models import UserSession

client = TestClient(app)


def test_root():
    assert client.get("/").status_code == 200


def test_uses_sqlite():
    assert "sqlite" in str(engine.url)


def test_session_can_be_created():
    with Session(engine) as session:
        session.add(UserSession())
        session.commit()
