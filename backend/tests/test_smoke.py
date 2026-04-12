from fastapi.testclient import TestClient
from sqlalchemy import text

from backend.app import app
from backend.database import engine

client = TestClient(app)


def test_root():
    assert client.get("/").status_code == 200

def test_db_connects():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
