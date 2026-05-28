from datetime import datetime
from typing import List, Optional

from sqlmodel import Session as DBSession, select

from backend.models import Message, Session


class SessionRepository:
    def __init__(self, db: DBSession) -> None:
        self.db = db

    # Creating a new session 
    def create(
        self,
        session_token: str,
        user_id: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Session:
        session = Session(session_token=session_token, user_id=user_id, title=title)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    # Finding a session by ID 
    def find_by_id(self, session_id: int) -> Optional[Session]:
        return self.db.get(Session, session_id)

    # Finding sessions by user 
    def find_by_user(self, user_id: str) -> List[Session]:
        return list(self.db.exec(select(Session).where(Session.user_id == user_id)).all())

    # Appending a message to a session 
    def append_message(self, session_id: int, content: str) -> Message:
        message = Message(content=content, session_id=session_id)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    # Retrieving the full message history of a session 
    def get_message_history(self, session_id: int) -> List[Message]:
        return list(
            self.db.exec(
                select(Message)
                .where(Message.session_id == session_id)
                .order_by(Message.created_at, Message.id)
            ).all()
        )

    # Updating session metadata 
    def update_metadata(
        self,
        session_id: int,
        title: Optional[str] = None,
        last_activity: Optional[datetime] = None,
    ) -> Optional[Session]:
        session = self.db.get(Session, session_id)
        if session is None:
            return None
        if title is not None:
            session.title = title
        if last_activity is not None:
            session.last_activity = last_activity
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    # Deleting a session 
    def delete(self, session_id: int) -> bool:
        session = self.db.get(Session, session_id)
        if session is None:
            return False
        self.db.delete(session)
        self.db.commit()
        return True
