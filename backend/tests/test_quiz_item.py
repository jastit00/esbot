import unittest
from datetime import timezone
from backend.models import QuizItem, QuizRequest, Session, SubmittedAnswer

class TestQuizItem(unittest.TestCase):

    def test_quiz_item_id_defaults_to_none(self):
        quiz_request = QuizRequest(topic="example topic", session=Session())
        quiz_item = QuizItem(text="example text", quiz_request=quiz_request)
        self.assertIsNone(quiz_item.id)


    def test_quiz_item_created_at_is_set_automatically(self):
        quiz_request = QuizRequest(topic="example topic", session=Session())
        quiz_item = QuizItem(text="example text", quiz_request=quiz_request)
        self.assertIsNotNone(quiz_item.created_at)


    def test_quiz_item_created_at_is_utc_aware(self):
        quiz_request = QuizRequest(topic="example topic", session=Session())
        quiz_item = QuizItem(text="example text", quiz_request=quiz_request)
        self.assertEqual(quiz_item.created_at.tzinfo, timezone.utc)


    def test_quiz_item_can_have_relationship(self):
        quiz_request = QuizRequest(topic="example topic", session=Session())
        quiz_item = QuizItem(text="example text", quiz_request=quiz_request)
        quiz_request.quiz_items = [quiz_item]

        self.assertEqual(len(quiz_request.quiz_items), 1)
        self.assertEqual(quiz_request.quiz_items[0], quiz_item)
        self.assertEqual(quiz_item.quiz_request, quiz_request)


    # SQLModel table=True bypasses Pydantic validation, so ValidationError is never raised.
    # Instead verify the nullable=False is correctly defined on the field.
    def test_quiz_item_text_is_required_and_non_nullable(self):
        field = QuizItem.model_fields["text"]
        self.assertTrue(field.is_required())
        self.assertFalse(field.nullable)

    def test_quiz_item_quiz_request_id_is_non_nullable(self):
        field = QuizItem.model_fields["quiz_request_id"]
        self.assertFalse(field.nullable)


    def test_quiz_item_can_have_multiple_submitted_answers(self):
        quiz_request = QuizRequest(topic="example topic", session=Session())
        quiz_item = QuizItem(text="example text", quiz_request=quiz_request)
        submitted_answer1 = SubmittedAnswer(text="test1", quiz_item=quiz_item)
        submitted_answer2 = SubmittedAnswer(text="test2", quiz_item=quiz_item)
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