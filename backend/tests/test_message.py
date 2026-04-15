import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import Message, UserSession

class TestMessage(unittest.TestCase):
    
    def test_message_id_defaults_to_none(self):
        user_session = UserSession()
        message = Message(content="example content", role="user", session=user_session)
        self.assertIsNone(message.id)


    def test_message_created_at_is_set_automatically(self):
        user_session = UserSession()
        message = Message(content="example content", role="user", session=user_session)
        self.assertIsNotNone(message.created_at)


    def test_message_created_at_is_utc_aware(self):
        user_session = UserSession()
        message = Message(content="example content", role="user", session=user_session)
        self.assertEqual(message.created_at.tzinfo, timezone.utc)


    def test_message_can_have_relationship(self):
        user_session = UserSession()
        message = Message(content="example content", role="user", session=user_session)
        user_session.messages = [message]

        self.assertEqual(len(user_session.messages), 1)
        self.assertEqual(user_session.messages[0], message)
        self.assertEqual(message.session, user_session)


    def test_message_content_not_null(self):
        user_session = UserSession()
        with self.assertRaises(ValidationError):
            Message(content=None, role="user", session=user_session)

    
    def test_message_role_not_null(self):
        user_session = UserSession()
        with self.assertRaises(ValidationError):
            Message(content="example content", role=None, session=user_session)
    

    def test_message_session_id_not_null(self):
        with self.assertRaises(ValidationError):
            Message(content="example content", role="user", session=None)


if __name__ == "__main__":
    unittest.main()



"""
Tool used: Windsurf Tab Completion, SWE-1.6
Purpose: Help with copy paste tasks (renaming methods); help with not null constraints
"""