# ESBot REST API Reference

This document describes the REST API exposed by the ESBot backend (Exercise 8.4)
and serves as the basis for the API testing performed in Exercise 10.

## Base URL

```
http://localhost:8000
```

The API is served by FastAPI/uvicorn. All endpoints accept and return JSON
(except `DELETE /sessions/{session_id}`, which has no response body).

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | Database connection string (required, no default) | `sqlite:///./local_test.db` or `postgresql://esbot_user:esbot_password@db:5432/esbot` |

> **LLM mock mode:** The endpoints currently implemented (sessions, message
> history, deletion) do not call the LLM inference engine, so no mock/stub
> configuration is required to run the API tests in this exercise.

## Setup Instructions (fresh checkout)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure the database connection (SQLite is sufficient for local testing,
   no PostgreSQL container required):
   ```bash
   export DATABASE_URL="sqlite:///./local_test.db"
   ```
   (PowerShell: `$env:DATABASE_URL = "sqlite:///./local_test.db"`)
3. Start the backend:
   ```bash
   uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
   ```
   Database tables are created automatically on startup.
4. Verify the liveness endpoint:
   ```bash
   curl http://localhost:8000/
   ```
   Expected response: `200 OK` with body `{"message": "Hello World"}`.

## Endpoints

### 1. `GET /` — Liveness check

Confirms the API is running.

- **Headers:** none required
- **Request body:** N/A
- **Success status:** `200 OK`
- **Example response:**
  ```json
  { "message": "Hello World" }
  ```

### 2. `POST /sessions` — Create a learning session

Creates a new learning session and returns its identifier and token.

- **Headers:** `Content-Type: application/json` (no body fields required)
- **Request body:** N/A (empty body)
- **Success status:** `201 Created`
- **Example response:**
  ```json
  {
    "id": 1,
    "session_token": "404da7d6-da3a-4ee1-8818-6f162a3fc392"
  }
  ```

### 3. `GET /sessions` — List sessions

Returns all learning sessions.

- **Headers:** none required
- **Request body:** N/A
- **Success status:** `200 OK`
- **Example response:**
  ```json
  [
    { "id": 1, "session_token": "404da7d6-da3a-4ee1-8818-6f162a3fc392" }
  ]
  ```

### 4. `GET /sessions/{session_id}/messages` — Retrieve message history

Returns the full message history of a session, ordered as stored.

- **Headers:** none required
- **Path parameters:** `session_id` (integer)
- **Request body:** N/A
- **Success status:** `200 OK`
- **Example response (no messages yet):**
  ```json
  []
  ```
- **Example response (with messages):**
  ```json
  [
    { "id": 1, "content": "Hello ESBot", "session_id": 1 }
  ]
  ```

### 5. `DELETE /sessions/{session_id}` — Delete a session

Deletes a session and all associated data (messages, quizzes) via cascading
delete.

- **Headers:** none required
- **Path parameters:** `session_id` (integer)
- **Request body:** N/A
- **Success status:** `204 No Content` (empty body)

## Error Responses

### 404 Not Found

Returned when a `session_id` does not exist (`GET /sessions/{session_id}/messages`,
`DELETE /sessions/{session_id}`).

```json
{ "error": "Session not found", "session_id": 999 }
```

### 422 Unprocessable Entity

Returned for invalid input, e.g. a non-integer `session_id` path parameter.

```json
{
  "error": "Invalid input",
  "details": [
    {
      "type": "int_parsing",
      "loc": ["path", "session_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```

### 500 Internal Server Error

Returned for unexpected, unhandled server errors (e.g. database connectivity
failure). No custom error body is registered for this case; FastAPI/Starlette
returns the default response:

```
Internal Server Error
```

with status code `500`.

### 503 Service Unavailable

Reserved for endpoints that depend on the LLM inference engine
(`LLMUnavailableError`). Not currently triggerable by the implemented
endpoints, but the handler is registered and returns:

```json
{ "error": "LLM inference engine is unreachable" }
```

## Endpoint Summary Table

| # | Method | Path | Description | Success Status |
|---|---|---|---|---|
| 1 | GET | `/` | Liveness check | 200 |
| 2 | POST | `/sessions` | Create a learning session | 201 |
| 3 | GET | `/sessions` | List all sessions | 200 |
| 4 | GET | `/sessions/{session_id}/messages` | Retrieve message history | 200 |
| 5 | DELETE | `/sessions/{session_id}` | Delete a session | 204 |
