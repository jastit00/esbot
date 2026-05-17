"""
REST API endpoints for ESBot.

Endpoints (4):
- POST   /sessions                       - create a new learning session
- GET    /sessions                       - list all sessions
- GET    /sessions/{session_id}/messages - retrieve message history of a session
- DELETE /sessions/{session_id}          - delete a session and its associated data

Error handling (5th scenario):
- 404 Not Found            - unknown session         (SessionNotFoundError)
- 422 Unprocessable Entity - invalid input           (FastAPI/Pydantic validation)
- 503 Service Unavailable  - LLM inference engine    (LLMUnavailableError)
"""

import uuid
from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session as DBSession, select

from backend.database import get_session
from backend.models import Session, Message

router = APIRouter(prefix="/sessions", tags=["sessions"])


# ---------- Schemas ----------

class SessionRead(BaseModel):
    id: int
    session_token: str

    class Config:
        from_attributes = True


class MessageRead(BaseModel):
    id: int
    content: str
    session_id: int

    class Config:
        from_attributes = True


# ---------- Custom exceptions ----------

class SessionNotFoundError(Exception):
    """Raised when a session id does not exist."""
    def __init__(self, session_id: int):
        self.session_id = session_id


class LLMUnavailableError(Exception):
    """Raised when the LLM inference engine is unreachable."""


# ---------- Endpoints ----------

# POST /sessions - create a new learning session
@router.post("", response_model=SessionRead, status_code=status.HTTP_201_CREATED)
def create_session(db: DBSession = Depends(get_session)) -> Session:
    session = Session(session_token=str(uuid.uuid4()))
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


# GET /sessions - list all sessions
@router.get("", response_model=List[SessionRead])
def list_sessions(db: DBSession = Depends(get_session)) -> List[Session]:
    return db.exec(select(Session)).all()


# GET /sessions/{session_id}/messages - retrieve message history of a session
@router.get("/{session_id}/messages", response_model=List[MessageRead])
def get_session_messages(session_id: int, db: DBSession = Depends(get_session)) -> List[Message]:
    if db.get(Session, session_id) is None:
        raise SessionNotFoundError(session_id)
    return db.exec(select(Message).where(Message.session_id == session_id)).all()


# DELETE /sessions/{session_id} - delete a session and its associated data
@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(session_id: int, db: DBSession = Depends(get_session)) -> None:
    session = db.get(Session, session_id)
    if session is None:
        raise SessionNotFoundError(session_id)
    db.delete(session)
    db.commit()


# ---------- Error handling registration ----------

def register_exception_handlers(app: FastAPI) -> None:
    """Register handlers mapping domain exceptions to HTTP responses."""

    @app.exception_handler(SessionNotFoundError)
    async def _session_not_found(_: Request, exc: SessionNotFoundError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"error": "Session not found", "session_id": exc.session_id},
        )

    @app.exception_handler(RequestValidationError)
    async def _invalid_input(_: Request, exc: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"error": "Invalid input", "details": exc.errors()},
        )

    @app.exception_handler(LLMUnavailableError)
    async def _llm_unavailable(_: Request, __: LLMUnavailableError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"error": "LLM inference engine is unreachable"},
        )

    @app.exception_handler(HTTPException)
    async def _http_exception(_: Request, exc: HTTPException) -> JSONResponse:
        return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


"""
Tool Used: Claude Opus 4.7
Purpose: Wurde ausschliesslich zur Syntax-Korrektur und zur strukturellen
        Unterstuetzung (z. B. korrekte FastAPI-Router-/Dependency-Syntax,
        Fehlerbehandlungs-Decorator-Syntax) eingesetzt.
"""


