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

| Method | Path | Headers | Body | Success |
|---|---|---|---|---|
| GET | `/api/v1/health` | none | N/A | 200 `{"status": "ok"}` |
| POST | `/sessions` | none | N/A (empty) | 201 `{"id": 1, "session_token": "..."}` |
| GET | `/sessions` | none | N/A | 200 `[{"id": 1, "session_token": "..."}]` |
| GET | `/sessions/{session_id}/messages` | none | N/A | 200 `[{"id": 1, "content": "...", "session_id": 1}]` |
| DELETE | `/sessions/{session_id}` | none | N/A | 204 (no body) |

## Errors

- **404** unknown `session_id`: `{"error": "Session not found", "session_id": 999}`
- **422** invalid input (e.g. non-integer `session_id`): `{"error": "Invalid input", "details": [...]}`
- **500** unhandled server error: `{"detail": "Internal Server Error"}`
- **503** LLM unavailable (handler registered, not yet triggerable): `{"error": "LLM inference engine is unreachable"}`
