import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import QuizItem, QuizRequest, UserSession, SubmittedAnswer

class TestQuizItem(unittest.TestCase):

    def test_quiz_item_id_defaults_to_none(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        self.assertIsNone(quiz_item.id)

    
    def test_quiz_item_created_at_is_set_automatically(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        self.assertIsNotNone(quiz_item.created_at)


    def test_quiz_item_created_at_is_utc_aware(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        self.assertEqual(quiz_item.created_at.tzinfo, timezone.utc)


    def test_quiz_item_can_have_relationship(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        user_session.quiz_items = [quiz_item]

        self.assertEqual(len(user_session.quiz_items), 1)
        self.assertEqual(user_session.quiz_items[0], quiz_item)
        self.assertEqual(quiz_item.session, user_session)


    def test_quiz_item_text_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        with self.assertRaises(ValidationError):
            QuizItem(text=None, session=user_session, quiz_request=quiz_request)


    def test_quiz_item_quiz_request_id_not_null(self):
        user_session = UserSession()
        with self.assertRaises(ValidationError):
            QuizItem(text="example text", session=user_session)


    def test_quiz_item_session_id_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        with self.assertRaises(ValidationError):
            QuizItem(text="example text", quiz_request=quiz_request)


    def test_quiz_item_can_have_multiple_submitted_answers(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer1 = SubmittedAnswer(text="test1", session=user_session, quiz_item=quiz_item)
        submitted_answer2 = SubmittedAnswer(text="test2", session=user_session, quiz_item=quiz_item)
        quiz_item.submitted_answers = [submitted_answer1, submitted_answer2]
        
        self.assertEqual(len(quiz_item.submitted_answers), 2)
        self.assertEqual(quiz_item.submitted_answers[0], submitted_answer1)
        self.assertEqual(quiz_item.submitted_answers[1], submitted_answer2)
        self.assertEqual(submitted_answer1.quiz_item, submitted_answer2.quiz_item)


if __name__ == "__main__":
    unittest.main()



"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""