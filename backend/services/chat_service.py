from typing import List, Optional

from backend.models import Session
from backend.services.question_service import AIInferenceInterface
from backend.services.session_repository import SessionRepository

FALLBACK_RESPONSE = "The AI service is currently unavailable. Please try again later."
FALLBACK_EVALUATION = "Unable to evaluate your answer at this time."


class ChatService:
    def __init__(self, session_repo: SessionRepository, ai_engine: AIInferenceInterface) -> None:
        self.session_repo = session_repo
        self.ai_engine = ai_engine

    def start_session(
        self,
        session_token: str,
        user_id: Optional[str] = None,
        title: Optional[str] = None,
    ) -> Session:
        return self.session_repo.create(session_token, user_id=user_id, title=title)

    def send_message(self, session_id: int, user_message: str) -> str:
        self.session_repo.append_message(session_id, user_message)
        try:
            response = self.ai_engine.generate_answer(user_message)
        except Exception:
            response = FALLBACK_RESPONSE
        self.session_repo.append_message(session_id, response)
        return response

    def generate_quiz(self, session_id: int, topic: str) -> List[str]:
        try:
            questions = self.ai_engine.generate_quiz(topic)
        except Exception:
            return []
        for question in questions:
            self.session_repo.append_message(session_id, question)
        return questions

    def evaluate_answer(self, session_id: int, question: str, user_answer: str) -> str:
        prompt = f"Question: {question}\nAnswer: {user_answer}"
        try:
            feedback = self.ai_engine.generate_answer(prompt)
        except Exception:
            feedback = FALLBACK_EVALUATION
        return feedback