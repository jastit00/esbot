import unittest
from datetime import timezone

from backend.models import UserSession, Message

class TestUserSessions(unittest.TestCase):

    def test_user_session_id_defaults_to_none(self):
        user_session = UserSession()
        self.assertIsNone(user_session.id)


    def test_user_session_created_at_is_set_automatically(self):
        user_session = UserSession()
        self.assertIsNotNone(user_session.created_at)


    def test_user_session_created_at_is_utc_aware(self):
        user_session = UserSession()
        self.assertEqual(user_session.created_at.tzinfo, timezone.utc)


    def test_user_session_can_have_relationship(self):
        user_session = UserSession()
        message = Message(content="example content", role="user", session=user_session)
        
        user_session.messages = [message]
        message.session = user_session
        
        self.assertEqual(len(user_session.messages), 1)
        self.assertEqual(user_session.messages[0], message)
        self.assertEqual(message.session, user_session)

    
    def test_user_session_can_have_multiple_messages(self):
        user_session = UserSession()
        message1 = Message(content="test1", role="user", session=user_session)
        message2 = Message(content="test2", role="admin", session=user_session)
        user_session.messages = [message1, message2]
        
        self.assertEqual(len(user_session.messages), 2)
        self.assertEqual(user_session.messages[0], message1)
        self.assertEqual(user_session.messages[1], message2)
        self.assertEqual(message1.session, message2.session)


if __name__ == "__main__":
    unittest.main()



"""
Tool Used: Windsurf SWE-1.6
Purpose: Help what can be compared in UserSession-Relationship Test
"""