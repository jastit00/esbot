from datetime import timezone

from backend.models import UserSession


def test_user_session_id_defaults_to_none():
    user_session = UserSession()
    assert user_session.id is None


def test_user_session_created_at_is_set_automatically():
    user_session = UserSession()
    assert user_session.created_at is not None


def test_user_session_created_at_is_utc_aware():
    user_session = UserSession()
    assert user_session.created_at.tzinfo == timezone.utc
