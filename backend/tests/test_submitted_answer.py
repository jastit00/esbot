import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import SubmittedAnswer, UserSession, QuizRequest, QuizItem

class TestSubmittedAnswer(unittest.TestCase):

    def test_submitted_answer_id_defaults_to_none(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        self.assertIsNone(submitted_answer.id)


    def test_submitted_answer_created_at_is_set_automatically(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        self.assertIsNotNone(submitted_answer.created_at)


    def test_submitted_answer_created_at_is_utc_aware(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        self.assertEqual(submitted_answer.created_at.tzinfo, timezone.utc)


    def test_submitted_answer_can_have_relationship(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        user_session.submitted_answers = [submitted_answer]

        self.assertEqual(len(user_session.submitted_answers), 1)
        self.assertEqual(user_session.submitted_answers[0], submitted_answer)
        self.assertEqual(submitted_answer.session, user_session)


    def test_submitted_answer_text_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        with self.assertRaises(ValidationError):
            SubmittedAnswer(text=None, session=user_session, quiz_item=quiz_item)


    def test_submitted_answer_quiz_item_id_not_null(self):
        user_session = UserSession()
        with self.assertRaises(ValidationError):
            SubmittedAnswer(text="example text", session=user_session)


    def test_submitted_answer_session_id_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        with self.assertRaises(ValidationError):
            SubmittedAnswer(text="example text", quiz_item=quiz_item)


if __name__ == "__main__":
    unittest.main()

    


"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""