import unittest
from datetime import timezone
from pydantic import ValidationError

from backend.models import QuizItem, QuizRequest, Session, SubmittedAnswer, FieldNotNullError

class TestQuizItem(unittest.TestCase):

    def test_quiz_item_id_defaults_to_none(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        self.assertIsNone(quiz_item.id)

    
    def test_quiz_item_created_at_is_set_automatically(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        self.assertIsNotNone(quiz_item.created_at)


    def test_quiz_item_created_at_is_utc_aware(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        self.assertEqual(quiz_item.created_at.tzinfo, timezone.utc)


    def test_quiz_item_can_have_relationship(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        session.quiz_items = [quiz_item]

        self.assertEqual(len(session.quiz_items), 1)
        self.assertEqual(session.quiz_items[0], quiz_item)
        self.assertEqual(quiz_item.session, session)


    def test_quiz_item_text_not_null(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        with self.assertRaises(FieldNotNullError):
            QuizItem(text=None, session=session, quiz_request=quiz_request)


    def test_quiz_item_quiz_request_id_not_null(self):
        session = Session()
        with self.assertRaises(FieldNotNullError):
            QuizItem(text="example text", session=session)


    def test_quiz_item_session_id_not_null(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        with self.assertRaises(FieldNotNullError):
            QuizItem(text="example text", quiz_request=quiz_request)


    def test_quiz_item_can_have_multiple_submitted_answers(self):
        session = Session()
        quiz_request = QuizRequest(topic="example topic", session=session)
        quiz_item = QuizItem(text="example text", session=session, quiz_request=quiz_request)
        submitted_answer1 = SubmittedAnswer(text="test1", session=session, quiz_item=quiz_item)
        submitted_answer2 = SubmittedAnswer(text="test2", session=session, quiz_item=quiz_item)
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