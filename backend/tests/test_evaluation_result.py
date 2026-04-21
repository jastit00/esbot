import unittest
from datetime import timezone
from backend.models import EvaluationResult, Session, QuizRequest, QuizItem, SubmittedAnswer

class TestEvaluationResult(unittest.TestCase):

    def test_evaluation_result_id_defaults_to_none(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertIsNone(evaluation_result.id)


    def test_evaluation_result_created_at_is_set_automatically(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertIsNotNone(evaluation_result.created_at)


    def test_evaluation_result_created_at_is_utc_aware(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)
        self.assertEqual(evaluation_result.created_at.tzinfo, timezone.utc)


    def test_evaluation_result_can_have_relationship(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        evaluation_result = EvaluationResult(is_correct=True, text="example text", submitted_answer=submitted_answer)

        self.assertEqual(evaluation_result.submitted_answer, submitted_answer)
        self.assertEqual(submitted_answer.evaluation_result, evaluation_result)


    # SQLModel table=True bypasses Pydantic validation, so ValidationError is never raised.
    # Instead verify the nullable=False is correctly defined on the field.
    def test_evaluation_result_text_is_required_and_non_nullable(self):
        field = EvaluationResult.model_fields["text"]
        self.assertTrue(field.is_required())
        self.assertFalse(field.nullable)

    def test_evaluation_result_is_correct_is_non_nullable(self):
        field = EvaluationResult.model_fields["is_correct"]
        self.assertFalse(field.nullable)

    def test_evaluation_result_submitted_answer_id_is_non_nullable(self):
        field = EvaluationResult.model_fields["submitted_answer_id"]
        self.assertFalse(field.nullable)


if __name__ == "__main__":
    unittest.main()

    

"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""