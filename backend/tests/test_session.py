import unittest
from datetime import timezone

from backend.models import Session, Message

class TestSessions(unittest.TestCase):

    def test_session_id_defaults_to_none(self):
        session = Session()
        self.assertIsNone(session.id)


    def test_session_created_at_is_set_automatically(self):
        session = Session()
        self.assertIsNotNone(session.created_at)


    def test_session_created_at_is_utc_aware(self):
        session = Session()
        self.assertEqual(session.created_at.tzinfo, timezone.utc)


    def test_session_can_have_relationship(self):
        session = Session()
        message = Message(content="example content", session=session)
        
        session.messages = [message]
        message.session = session
        
        self.assertEqual(len(session.messages), 1)
        self.assertEqual(session.messages[0], message)
        self.assertEqual(message.session, session)

    
    def test_session_can_have_multiple_messages(self):
        session = Session()
        message1 = Message(content="test1", session=session)
        message2 = Message(content="test2", session=session)
        session.messages = [message1, message2]
        
        self.assertEqual(len(session.messages), 2)
        self.assertEqual(session.messages[0], message1)
        self.assertEqual(session.messages[1], message2)
        self.assertEqual(message1.session, message2.session)


if __name__ == "__main__":
    unittest.main()



"""
Tool Used: Windsurf SWE-1.6
Purpose: Help what can be compared in Session-Relationship Test
"""