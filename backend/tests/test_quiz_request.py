import unittest
from datetime import timezone
from backend.models import QuizRequest, QuizItem, Session

class TestQuizRequest(unittest.TestCase):

    def test_quiz_request_id_defaults_to_none(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        self.assertIsNone(quiz_request.id)

    
    def test_quiz_request_created_at_is_set_automatically(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        self.assertIsNotNone(quiz_request.created_at)


    def test_quiz_request_created_at_is_utc_aware(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        self.assertEqual(quiz_request.created_at.tzinfo, timezone.utc)


    def test_quiz_request_can_have_relationship(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        session.quiz_requests = [quiz_request]

        self.assertEqual(len(session.quiz_requests), 1)
        self.assertEqual(session.quiz_requests[0], quiz_request)
        self.assertEqual(quiz_request.session, session)


    # SQLModel table=True bypasses Pydantic validation, so ValidationError is never raised.
    # Instead verify the nullable=False is correctly defined on the field.
    def test_quiz_request_topic_is_required_and_non_nullable(self):
        field = QuizRequest.model_fields["topic"]
        self.assertTrue(field.is_required())
        self.assertFalse(field.nullable)

    def test_quiz_request_session_id_is_non_nullable(self):
        field = QuizRequest.model_fields["session_id"]
        self.assertFalse(field.nullable)


    def test_quiz_request_can_have_multiple_quiz_items(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item1 = QuizItem(text="test1", session=session, quiz_request=quiz_request)
        quiz_item2 = QuizItem(text="test2", session=session, quiz_request=quiz_request)
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