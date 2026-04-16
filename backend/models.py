"""
ai wurde für syntax verwendet
"""

from typing import List, Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Relationship
from pydantic import field_validator

class FieldNotNullError(ValueError):
    """Exception raised when a required field is None"""
    pass

def validate_not_null(v):
    if v is None:
        raise FieldNotNullError('Field cannot be None')
    return v

class Session(SQLModel, table=True):
    __tablename__ = "sessions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    
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
    
    @field_validator('content', 'session_id', 'created_at')
    @classmethod
    def check_not_null(cls, v):
        return validate_not_null(v)

class QuizRequest(SQLModel, table=True):
    __tablename__ = "quiz_requests"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    
    session_id: int = Field(foreign_key="sessions.id", nullable=False)
    session: Session = Relationship(back_populates="quiz_requests")
    quiz_items: List["QuizItem"] = Relationship(back_populates="quiz_request")
    
    @field_validator('topic', 'session_id', 'created_at')
    @classmethod
    def check_not_null(cls, v):
        return validate_not_null(v)

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
    
    @field_validator('text', 'session_id', 'quiz_request_id', 'created_at')
    @classmethod
    def check_not_null(cls, v):
        return validate_not_null(v)

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
    
    @field_validator('text', 'session_id', 'quiz_item_id', 'created_at')
    @classmethod
    def check_not_null(cls, v):
        return validate_not_null(v)

class EvaluationResult(SQLModel, table=True):
    __tablename__ = "evaluation_results"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    is_correct: bool = Field(nullable=False)
    text: str = Field(min_length=1, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    
    submitted_answer_id: int = Field(foreign_key="submitted_answers.id", unique=True, nullable=False)
    submitted_answer: SubmittedAnswer = Relationship(back_populates="evaluation_result")
    
    @field_validator('is_correct', 'text', 'submitted_answer_id', 'created_at')
    @classmethod
    def check_not_null(cls, v):
        return validate_not_null(v)



"""
Tool Used: Windsurf SWE-1.6 & Tab Completion
Purpose: Help writing validate_not_null function & field validators
"""