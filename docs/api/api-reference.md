# ESBot REST API Reference

Base URL: `http://localhost:8000`

## Setup

```bash
pip install -r requirements.txt
export DATABASE_URL="sqlite:///./local_test.db"
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
curl http://localhost:8000/api/v1/health   # -> 200 {"status": "ok"}
```

## Endpoints

| Method | Path | Body | Success |
|--------|------|------|---------|
| GET | `/api/v1/health` | — | 200 `{"status": "ok"}` |
| POST | `/api/v1/sessions` | `{"user_id": "alice"}` (optional) | 201 `{"id": 1, "session_token": "...", "user_id": "alice"}` |
| GET | `/api/v1/sessions` | — | 200 `[{"id": 1, "session_token": "...", "user_id": "alice"}]` |
| GET | `/api/v1/sessions?user_id=alice` | — | 200 (filtered by user) |
| GET | `/api/v1/sessions/{session_id}/messages` | — | 200 `[{"id": 1, "content": "...", "session_id": 1}]` |
| DELETE | `/api/v1/sessions/{session_id}` | — | 204 (no body) |
| POST | `/api/v1/sessions/{session_id}/messages` | `{"content": "Hello"}` | 201 `{"user_message": {...}, "assistant_message": {...}}` |
| POST | `/api/v1/sessions/{session_id}/quiz` | `{"topic": "Testing"}` | 201 `{"questions": ["...", "..."]}` |

## Errors

- **404** unknown `session_id`: `{"error": "Session not found", "session_id": 999}`
- **422** invalid input (e.g. non-integer `session_id`): `{"error": "Invalid input", "details": [...]}`
- **503** LLM unavailable: `{"error": "LLM inference engine is unreachable"}`
