from backend.services.question_service import (
    MockAIInference,
    QuestionService,
    QuizService,
)


def before_scenario(context, scenario):
    context.ai = MockAIInference()
    context.question_service = QuestionService(context.ai)
    context.quiz_service = QuizService(context.ai)
    context.session_history = []
    context.materials = []


def after_scenario(context, scenario):
    context.session_history.clear()
    context.materials.clear()
