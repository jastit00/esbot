"""
Automated API tests for ESBot endpoints.

Tests cover happy-path workflows and negative/edge cases using pytest and FastAPI TestClient.
Uses in-memory SQLite for test isolation.
"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session
from sqlmodel.pool import StaticPool

from backend.app import app
from backend.database import get_session
from backend.models import Session as SessionModel, Message


# ---------- Test Database Setup ----------

@pytest.fixture(name="session")
def session_fixture():
    """Create an in-memory SQLite database for testing."""
    engine = create_engine(
        "sqlite:///:memory:",
        #"sqlite:///test_db.sqlite",
        connect_args={"check_same_thread": False},  # Allow connections from multiple threads
        poolclass=StaticPool,                       # Use a static pool instead of a connection pool
    )
    
    # Create tables in the database
    from backend.models import SQLModel
    SQLModel.metadata.create_all(engine)
    
    # Use a session context manager to ensure the database is closed
    with Session(engine) as session:
        yield session  # Return the session object from the context manager


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Create a test client with the test database session."""
    # Override the get_session dependency to use the test database session
    def override_get_session():
        yield session
    
    app.dependency_overrides[get_session] = override_get_session
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


# ---------- Happy Path Tests ----------

def test_health_endpoint(client: TestClient):
    """Test the health endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_session_creation(client: TestClient):
    """Test session creation."""
    response = client.post("/api/v1/sessions")
    assert response.status_code == 201

    data = response.json()["session_token"] 
    assert len(data) > 0


def test_session_listing(client: TestClient):
    """Test session listing."""
    # Create a session first
    created_response = client.post("/api/v1/sessions")
    session_id = created_response.json()["id"]

    response = client.get("/api/v1/sessions")
    assert response.status_code == 200

    data = response.json()
    assert len(data) > 0
    assert isinstance(data, list)
    assert data[0]["id"] == session_id
    #print("JSON response:", response.json())
    #[{'id': 1, 'session_token': '7b75c12e-9528-4fb0-ab19-1468054b70c1'}]


def test_message_history_retrieval(client: TestClient):
    """Test message history retrieval."""
    # Create a session first
    created_response = client.post("/api/v1/sessions")
    session_id = created_response.json()["id"]

    response = client.get(f"/api/v1/sessions/{session_id}/messages")
    assert response.status_code == 200

    messages = response.json()
    assert isinstance(messages, list)
    assert len(messages) == 0


def test_session_deletion(client: TestClient):
    """Test session deletion."""
    # Create a session first
    created_response = client.post("/api/v1/sessions")
    session_id = created_response.json()["id"]

    response = client.delete(f"/api/v1/sessions/{session_id}")
    assert response.status_code == 204

    empty_response = client.get(f"/api/v1/sessions")
    data = empty_response.json()
    assert len(data) == 0


# ---------- Negative / Edge Case Tests ----------

def test_session_not_found(client: TestClient):
    """Test session not found."""
    session_id = 31415
    response = client.get(f"/api/v1/sessions/{session_id}/messages")
    assert response.status_code == 404

    data = response.json()
    assert data["error"] == "Session not found"


def test_session_get_no_messages(client: TestClient):
    """Test GET on messages before any message is sent."""
    # Create a session first
    created_response = client.post("/api/v1/sessions")
    session_id = created_response.json()["id"]

    response = client.get(f"/api/v1/sessions/{session_id}/messages")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_non_exisiting_session_deletion(client: TestClient):
    """Test deleting a non existing session."""
    session_id = 31415
    response = client.delete(f"/api/v1/sessions/{session_id}")
    assert response.status_code == 404

    data = response.json()
    assert data["error"] == "Session not found"


def test_invalid_session_id_format(client: TestClient):
    """Test invalid format of session id"""
    session_id = "wrong_format"
    response = client.get(f"/api/v1/sessions/{session_id}/messages")
    assert response.status_code == 422

    data = response.json()
    assert data["error"] == "Invalid input"



"""
Tool Used: SWE-1.6 Slow
Purpose: SWE wurde als Starthilfe eingesetzt, um zu verstehen, wie man startet und was man beachten muss.
         Außerdem wurde SWE zur Unsterstützung zum Fehlerbeheben, zur Methoden-Syntax und bei dem Erstellen des Test Setups eingesetzt.
"""