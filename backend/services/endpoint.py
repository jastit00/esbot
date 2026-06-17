"""
REST API endpoints for ESBot.

Endpoints:
- POST   /api/v1/sessions                            - create a new learning session
- GET    /api/v1/sessions                            - list all sessions
- GET    /api/v1/sessions/{session_id}/messages      - retrieve message history of a session
- DELETE /api/v1/sessions/{session_id}               - delete a session and its associated data
- POST   /api/v1/sessions/{session_id}/messages      - send a message and receive an AI response
- POST   /api/v1/sessions/{session_id}/quiz          - generate quiz questions for a topic

Error handling:
- 404 Not Found            - unknown session         (SessionNotFoundError)
- 422 Unprocessable Entity - invalid input           (FastAPI/Pydantic validation)
- 503 Service Unavailable  - LLM inference engine    (LLMUnavailableError)
"""

import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlmodel import Session as DBSession, select

from backend.database import get_session
from backend.models import Session, Message
from backend.services.question_service import MockAIInference

_mock_ai = MockAIInference()

router = APIRouter(prefix="/sessions", tags=["sessions"])


# ---------- Schemas ----------

class SessionCreate(BaseModel):
    user_id: Optional[str] = None


class SessionRead(BaseModel):
    id: int
    session_token: str
    user_id: Optional[str] = None

    class Config:
        from_attributes = True


class MessageRead(BaseModel):
    id: int
    content: str
    session_id: int

    class Config:
        from_attributes = True


class MessageCreate(BaseModel):
    content: str


class ChatResponse(BaseModel):
    user_message: MessageRead
    assistant_message: MessageRead


class QuizCreate(BaseModel):
    topic: str


class QuizResponse(BaseModel):
    questions: List[str]


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
def create_session(body: Optional[SessionCreate] = None, db: DBSession = Depends(get_session)) -> Session:
    body = body or SessionCreate()
    session = Session(session_token=str(uuid.uuid4()), user_id=body.user_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


# GET /sessions - list all sessions, optionally filtered by user_id
@router.get("", response_model=List[SessionRead])
def list_sessions(user_id: Optional[str] = None, db: DBSession = Depends(get_session)) -> List[Session]:
    query = select(Session)
    if user_id:
        query = query.where(Session.user_id == user_id)
    return db.exec(query).all()


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


# POST /sessions/{session_id}/messages - send a message and receive an AI response
@router.post("/{session_id}/messages", response_model=ChatResponse, status_code=status.HTTP_201_CREATED)
def send_message(session_id: int, body: MessageCreate, db: DBSession = Depends(get_session)) -> ChatResponse:
    if db.get(Session, session_id) is None:
        raise SessionNotFoundError(session_id)
    user_msg = Message(content=body.content, session_id=session_id)
    db.add(user_msg)
    db.commit()
    db.refresh(user_msg)
    ai_text = _mock_ai.generate_answer(body.content)
    bot_msg = Message(content=ai_text, session_id=session_id)
    db.add(bot_msg)
    db.commit()
    db.refresh(bot_msg)
    return ChatResponse(
        user_message=MessageRead.model_validate(user_msg),
        assistant_message=MessageRead.model_validate(bot_msg),
    )


# POST /sessions/{session_id}/quiz - generate quiz questions for a topic
@router.post("/{session_id}/quiz", response_model=QuizResponse, status_code=status.HTTP_201_CREATED)
def generate_quiz(session_id: int, body: QuizCreate, db: DBSession = Depends(get_session)) -> QuizResponse:
    if db.get(Session, session_id) is None:
        raise SessionNotFoundError(session_id)
    questions = _mock_ai.generate_quiz(body.topic)
    return QuizResponse(questions=questions)


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


