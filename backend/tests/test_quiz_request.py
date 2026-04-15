import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import QuizRequest, QuizItem, UserSession

class TestQuizRequest(unittest.TestCase):

    def test_quiz_request_id_defaults_to_none(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        self.assertIsNone(quiz_request.id)

    
    def test_quiz_request_created_at_is_set_automatically(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        self.assertIsNotNone(quiz_request.created_at)


    def test_quiz_request_created_at_is_utc_aware(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        self.assertEqual(quiz_request.created_at.tzinfo, timezone.utc)


    def test_quiz_request_can_have_relationship(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        user_session.quiz_requests = [quiz_request]

        self.assertEqual(len(user_session.quiz_requests), 1)
        self.assertEqual(user_session.quiz_requests[0], quiz_request)
        self.assertEqual(quiz_request.session, user_session)


    def test_quiz_request_topic_not_null(self):
        user_session = UserSession()
        with self.assertRaises(ValidationError):
            QuizRequest(topic=None, session=user_session)


    def test_quiz_request_session_id_not_null(self):
        with self.assertRaises(ValidationError):
            QuizRequest(topic="example topic")


    def test_quiz_request_can_have_multiple_quiz_items(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item1 = QuizItem(text="test1", session=user_session, quiz_request=quiz_request)
        quiz_item2 = QuizItem(text="test2", session=user_session, quiz_request=quiz_request)
        quiz_request.quiz_items = [quiz_item1, quiz_item2]
        
        self.assertEqual(len(quiz_request.quiz_items), 2)
        self.assertEqual(quiz_request.quiz_items[0], quiz_item1)
        self.assertEqual(quiz_request.quiz_items[1], quiz_item2)
        self.assertEqual(quiz_item1.quiz_request, quiz_item2.quiz_request)


if __name__ == "__main__":
    unittest.main()



"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""