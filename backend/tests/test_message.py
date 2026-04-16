import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import Message, Session, FieldNotNullError

class TestMessage(unittest.TestCase):
    
    def test_message_id_defaults_to_none(self):
        session = Session()
        message = Message(content="example content", session=session)
        self.assertIsNone(message.id)


    def test_message_created_at_is_set_automatically(self):
        session = Session()
        message = Message(content="example content", session=session)
        self.assertIsNotNone(message.created_at)


    def test_message_created_at_is_utc_aware(self):
        session = Session()
        message = Message(content="example content", session=session)
        self.assertEqual(message.created_at.tzinfo, timezone.utc)


    def test_message_can_have_relationship(self):
        session = Session()
        message = Message(content="example content", session=session)
        session.messages = [message]

        self.assertEqual(len(session.messages), 1)
        self.assertEqual(session.messages[0], message)
        self.assertEqual(message.session, session)


    def test_message_content_not_null(self):
        session = Session()
        with self.assertRaises(FieldNotNullError):
            Message(content=None, session=session)
    

    def test_message_session_id_not_null(self):
        with self.assertRaises(FieldNotNullError):
            Message(content="example content", session=None)


if __name__ == "__main__":
    unittest.main()



"""
Tool used: Windsurf Tab Completion, SWE-1.6
Purpose: Help with copy paste tasks (renaming methods); help with not null constraints
"""