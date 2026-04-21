import unittest
from datetime import timezone
from backend.models import SubmittedAnswer, Session, QuizRequest, QuizItem

class TestSubmittedAnswer(unittest.TestCase):

    def test_submitted_answer_id_defaults_to_none(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        self.assertIsNone(submitted_answer.id)


    def test_submitted_answer_created_at_is_set_automatically(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        self.assertIsNotNone(submitted_answer.created_at)


    def test_submitted_answer_created_at_is_utc_aware(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        self.assertEqual(submitted_answer.created_at.tzinfo, timezone.utc)


    def test_submitted_answer_can_have_relationship(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer = SubmittedAnswer(text="example text", session=session, quiz_item=quiz_item)
        session.submitted_answers = [submitted_answer]

        self.assertEqual(len(session.submitted_answers), 1)
        self.assertEqual(session.submitted_answers[0], submitted_answer)
        self.assertEqual(submitted_answer.session, session)


    # SQLModel table=True bypasses Pydantic validation, so ValidationError is never raised.
    # Instead verify the nullable=False is correctly defined on the field.
    def test_submitted_answer_text_is_required_and_non_nullable(self):
        field = SubmittedAnswer.model_fields["text"]
        self.assertTrue(field.is_required())
        self.assertFalse(field.nullable)

    def test_submitted_answer_session_id_is_non_nullable(self):
        field = SubmittedAnswer.model_fields["session_id"]
        self.assertFalse(field.nullable)

    def test_submitted_answer_quiz_item_id_is_non_nullable(self):
        field = SubmittedAnswer.model_fields["quiz_item_id"]
        self.assertFalse(field.nullable)


if __name__ == "__main__":
    unittest.main()

    


"""
Tool used: Windsurf Tab Completion
Purpose: Help with copy paste tasks (renaming methods)
"""