from typing import Protocol, List

class AIInferenceInterface(Protocol):
    def generate_answer(self, prompt: str) -> str:
        ...

class MockAIInference(AIInferenceInterface):
    def __init__(self):
        self.should_fail = False
        self.should_be_off_topic = False
        self.last_prompt = None

    def generate_answer(self, prompt: str) -> str:
        self.last_prompt = prompt
        if self.should_fail:
            raise Exception("AI retrieval failed")
        if self.should_be_off_topic:
            return "This is an off-topic answer."
        return "This is a clear, contextual explanation based on the material."

class QuestionService:
    def __init__(self, ai_engine: AIInferenceInterface):
        self.ai_engine = ai_engine

    def handle_question(self, question: str, context: str) -> str:
        # Business logic for prompt construction
        prompt = f"Context: {context}\nQuestion: {question}"
        return self.ai_engine.generate_answer(prompt)
