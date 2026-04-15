import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import EvaluationResult, UserSession, QuizRequest, QuizItem, SubmittedAnswer

class TestEvaluationResult(unittest.TestCase):

    def test_evaluation_result_id_defaults_to_none(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertIsNone(evaluation_result.id)


    def test_evaluation_result_created_at_is_set_automatically(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertIsNotNone(evaluation_result.created_at)


    def test_evaluation_result_created_at_is_utc_aware(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertEqual(evaluation_result.created_at.tzinfo, timezone.utc)


    def test_evaluation_result_can_have_relationship(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)

        self.assertEqual(evaluation_result.submitted_answer, submitted_answer)
        self.assertEqual(submitted_answer.evaluation_result, evaluation_result)


    def test_evaluation_result_text_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        with self.assertRaises(ValidationError):
            EvaluationResult(is_correct=True, text=None, submitted_answer=submitted_answer)


    def test_evaluation_result_is_correct_not_null(self):
        user_session = UserSession()
        quiz_request = QuizRequest(topic="example topic", session=user_session)
        quiz_item = QuizItem(text="example text", session=user_session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=user_session, quiz_item=quiz_item)
        with self.assertRaises(ValidationError):
            EvaluationResult(text="example text", submitted_answer=submitted_answer)


    def test_evaluation_result_submitted_answer_id_not_null(self):
        with self.assertRaises(ValidationError):
            EvaluationResult(is_correct=True, text="example text", submitted_answer=None)


if __name__ == "__main__":
    unittest.main()

    

"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""