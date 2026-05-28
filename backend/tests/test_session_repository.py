from datetime import datetime
from sqlmodel import Session as DBSession
from backend.models import Message, Session as SessionModel
from backend.services.session_repository import SessionRepository


# 1. Creating a new session
def test_create_persists_session(session: DBSession):
    repo = SessionRepository(session)

    result = repo.create("abc123", user_id="alice", title="test")

    db_record = session.get(SessionModel, result.id)
    assert db_record is not None
    assert db_record.session_token == "abc123"


# 2. Finding a session by ID
def test_find_by_id(session: DBSession):
    repo = SessionRepository(session)
    created = repo.create("abc123")

    found = repo.find_by_id(created.id)

    assert found is not None
    assert found.id == created.id


# 3. Finding sessions by user
def test_find_by_user(session: DBSession):
    repo = SessionRepository(session)
    repo.create("abc123", user_id="alice")
    repo.create("def456", user_id="alice")
    repo.create("ghi789", user_id="bob")

    results = repo.find_by_user("alice")

    assert len(results) == 2


# 4. Appending a message to a session
def test_append_message(session: DBSession):
    repo = SessionRepository(session)
    s = repo.create("abc123")

    msg = repo.append_message(s.id, "message")

    db_msg = session.get(Message, msg.id)
    assert db_msg is not None
    assert db_msg.content == "message"
    assert db_msg.session_id == s.id


# 5. Retrieving the full message history
def test_get_message_history(session: DBSession):
    repo = SessionRepository(session)
    s = repo.create("abc123")
    repo.append_message(s.id, "message1")
    repo.append_message(s.id, "message2")
    repo.append_message(s.id, "message3")

    history = repo.get_message_history(s.id)

    assert len(history) == 3
    assert [m.content for m in history] == ["message1", "message2", "message3"]


# 6. Updating session metadata
def test_update_metadata(session: DBSession):
    repo = SessionRepository(session)
    s = repo.create("abc123", title="title1")

    repo.update_metadata(s.id, title="title2")

    db_record = session.get(SessionModel, s.id)
    assert db_record.title == "title2"


# 7. Deleting a session
def test_delete(session: DBSession):
    repo = SessionRepository(session)
    s = repo.create("abc123")
    msg = repo.append_message(s.id, "message")
    session_id = s.id
    msg_id = msg.id

    repo.delete(session_id)

    assert session.get(SessionModel, session_id) is None
    assert session.get(Message, msg_id) is None