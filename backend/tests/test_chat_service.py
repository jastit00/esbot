from unittest.mock import MagicMock

import pytest

from backend.models import Session
from backend.services.chat_service import (
    FALLBACK_EVALUATION,
    FALLBACK_RESPONSE,
    ChatService,
)


@pytest.fixture
def mock_repo():
    return MagicMock()


@pytest.fixture
def mock_ai():
    return MagicMock()


@pytest.fixture
def chat_service(mock_repo, mock_ai):
    return ChatService(session_repo=mock_repo, ai_engine=mock_ai)


# ---------------------------------------------------------------------------
# 1. Start a new learning session
# ---------------------------------------------------------------------------

def test_start_session_delegates_to_repository(chat_service, mock_repo):
    mock_session = MagicMock(spec=Session)
    mock_repo.create.return_value = mock_session

    result = chat_service.start_session("tok123", user_id="alice", title="Python Basics")

    mock_repo.create.assert_called_once_with("tok123", user_id="alice", title="Python Basics")
    assert result is mock_session


def test_start_session_without_optional_fields(chat_service, mock_repo):
    mock_repo.create.return_value = MagicMock(spec=Session)

    chat_service.start_session("tok456")

    mock_repo.create.assert_called_once_with("tok456", user_id=None, title=None)


# ---------------------------------------------------------------------------
# 2. Send a message and receive a response
# ---------------------------------------------------------------------------

def test_send_message_stores_user_message_then_ai_response(chat_service, mock_repo, mock_ai):
    mock_ai.generate_answer.return_value = "Some AI response"

    chat_service.send_message(session_id=1, user_message="What is recursion?")

    calls = mock_repo.append_message.call_args_list
    assert len(calls) == 2
    assert calls[0].args == (1, "What is recursion?")
    assert calls[1].args == (1, "Some AI response")


def test_send_message_returns_ai_response(chat_service, mock_repo, mock_ai):
    mock_ai.generate_answer.return_value = "Recursion is self-referential."

    response = chat_service.send_message(session_id=1, user_message="What is recursion?")

    assert response == "Recursion is self-referential."


def test_send_message_forwards_user_message_to_llm(chat_service, mock_repo, mock_ai):
    mock_ai.generate_answer.return_value = "answer"

    chat_service.send_message(session_id=1, user_message="Explain OOP")

    mock_ai.generate_answer.assert_called_once_with("Explain OOP")


# ---------------------------------------------------------------------------
# 3. LLM service failure – fallback response
# ---------------------------------------------------------------------------

def test_send_message_returns_fallback_on_llm_failure(chat_service, mock_repo, mock_ai):
    mock_ai.generate_answer.side_effect = Exception("LLM unreachable")

    response = chat_service.send_message(session_id=1, user_message="What is recursion?")

    assert response == FALLBACK_RESPONSE


def test_send_message_still_stores_two_messages_on_llm_failure(chat_service, mock_repo, mock_ai):
    mock_ai.generate_answer.side_effect = Exception("LLM unreachable")

    chat_service.send_message(session_id=1, user_message="What is recursion?")

    assert mock_repo.append_message.call_count == 2
    mock_repo.append_message.assert_any_call(1, "What is recursion?")
    mock_repo.append_message.assert_any_call(1, FALLBACK_RESPONSE)


# ---------------------------------------------------------------------------
# 4. Generate a quiz
# ---------------------------------------------------------------------------

def test_generate_quiz_returns_questions_from_llm(chat_service, mock_repo, mock_ai):
    mock_ai.generate_quiz.return_value = ["Q1?", "Q2?", "Q3?"]

    questions = chat_service.generate_quiz(session_id=1, topic="Sorting Algorithms")

    assert questions == ["Q1?", "Q2?", "Q3?"]


def test_generate_quiz_passes_topic_to_llm(chat_service, mock_repo, mock_ai):
    mock_ai.generate_quiz.return_value = []

    chat_service.generate_quiz(session_id=1, topic="Binary Trees")

    mock_ai.generate_quiz.assert_called_once_with("Binary Trees")


def test_generate_quiz_stores_each_question_in_session(chat_service, mock_repo, mock_ai):
    mock_ai.generate_quiz.return_value = ["Q1?", "Q2?"]

    chat_service.generate_quiz(session_id=5, topic="Graphs")

    assert mock_repo.append_message.call_count == 2
    mock_repo.append_message.assert_any_call(5, "Q1?")
    mock_repo.append_message.assert_any_call(5, "Q2?")


# ---------------------------------------------------------------------------
# 5. LLM service failure during quiz generation
# ---------------------------------------------------------------------------

def test_generate_quiz_returns_empty_list_on_llm_failure(chat_service, mock_repo, mock_ai):
    mock_ai.generate_quiz.side_effect = Exception("AI engine down")

    questions = chat_service.generate_quiz(session_id=1, topic="Sorting Algorithms")

    assert questions == []


def test_generate_quiz_stores_nothing_on_llm_failure(chat_service, mock_repo, mock_ai):
    mock_ai.generate_quiz.side_effect = Exception("AI engine down")

    chat_service.generate_quiz(session_id=1, topic="Sorting Algorithms")

    mock_repo.append_message.assert_not_called()


# ---------------------------------------------------------------------------
# 6. Evaluate a user answer
# ---------------------------------------------------------------------------

def test_evaluate_answer_includes_question_and_answer_in_llm_prompt(chat_service, mock_ai):
    mock_ai.generate_answer.return_value = "Correct!"

    chat_service.evaluate_answer(
        session_id=1,
        question="What is a stack?",
        user_answer="A LIFO data structure",
    )

    prompt = mock_ai.generate_answer.call_args[0][0]
    assert "What is a stack?" in prompt
    assert "A LIFO data structure" in prompt


def test_evaluate_answer_returns_llm_feedback(chat_service, mock_ai):
    mock_ai.generate_answer.return_value = "Correct! A stack is indeed LIFO."

    feedback = chat_service.evaluate_answer(
        session_id=1,
        question="What is a stack?",
        user_answer="A LIFO data structure",
    )

    assert feedback == "Correct! A stack is indeed LIFO."


# ---------------------------------------------------------------------------
# 7. LLM service failure during answer evaluation
# ---------------------------------------------------------------------------

def test_evaluate_answer_returns_fallback_on_llm_failure(chat_service, mock_ai):
    mock_ai.generate_answer.side_effect = Exception("LLM timeout")

    feedback = chat_service.evaluate_answer(
        session_id=1,
        question="What is a stack?",
        user_answer="I don't know",
    )

    assert feedback == FALLBACK_EVALUATION


"""""
Tool Used: Claude Code with Sonnet 4.6
Purpose: Generate Tests for ChatService

"""""