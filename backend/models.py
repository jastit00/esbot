"""
ai wurde für syntax verwendet
"""

from typing import List, Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship


class Session(SQLModel, table=True):
    __tablename__ = "sessions"

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    session_token: str = Field(index=True, unique=True, nullable=False)

    messages: List["Message"] = Relationship(back_populates="session")
    quiz_requests: List["QuizRequest"] = Relationship(back_populates="session")
    quiz_items: List["QuizItem"] = Relationship(back_populates="session")
    submitted_answers: List["SubmittedAnswer"] = Relationship(back_populates="session")


class Message(SQLModel, table=True):
    __tablename__ = "messages"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    session_id: int = Field(foreign_key="sessions.id", nullable=False)
    session: Session = Relationship(back_populates="messages")


class QuizRequest(SQLModel, table=True):
    __tablename__ = "quiz_requests"

    id: Optional[int] = Field(default=None, primary_key=True)
    topic: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    session_id: int = Field(foreign_key="sessions.id", nullable=False)
    session: Session = Relationship(back_populates="quiz_requests")
    quiz_items: List["QuizItem"] = Relationship(back_populates="quiz_request")


class QuizItem(SQLModel, table=True):
    __tablename__ = "quiz_items"

    id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    session_id: int = Field(foreign_key="sessions.id", nullable=False)
    quiz_request_id: int = Field(foreign_key="quiz_requests.id", nullable=False)

    session: Session = Relationship(back_populates="quiz_items")
    quiz_request: QuizRequest = Relationship(back_populates="quiz_items")
    submitted_answers: List["SubmittedAnswer"] = Relationship(back_populates="quiz_item")


class SubmittedAnswer(SQLModel, table=True):
    __tablename__ = "submitted_answers"

    id: Optional[int] = Field(default=None, primary_key=True)
    text: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    session_id: int = Field(foreign_key="sessions.id", nullable=False)
    quiz_item_id: int = Field(foreign_key="quiz_items.id", nullable=False)

    session: Session = Relationship(back_populates="submitted_answers")
    quiz_item: QuizItem = Relationship(back_populates="submitted_answers")
    evaluation_result: Optional["EvaluationResult"] = Relationship(
        back_populates="submitted_answer",
        sa_relationship_kwargs={"uselist": False}
    )


class EvaluationResult(SQLModel, table=True):
    __tablename__ = "evaluation_results"

    id: Optional[int] = Field(default=None, primary_key=True)
    is_correct: bool = Field(nullable=False)
    text: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)

    submitted_answer_id: int = Field(foreign_key="submitted_answers.id", unique=True, nullable=False)
    submitted_answer: SubmittedAnswer = Relationship(back_populates="evaluation_result")


"""
Tool Used: Windsurf SWE-1.6 & Tab Completion
Purpose: Help writing validate_not_null function & field validators

Tool Used: GPT-5.3-Codex
Purpose: Syntax-Vervollstaendigung und als Unterstuetzung bei der Strukturierung von Modellklassen
"""
