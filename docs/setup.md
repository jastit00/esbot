# Backend

## Tech Stack

| Concern | Choice |
|---|---|
| Framework | FastAPI |
| ASGI server | uvicorn |
| ORM / persistence | SQLAlchemy |
| Database (production) | PostgreSQL |
| Database (tests) | SQLite in-memory |
| Test framework | pytest |

## Prerequisites

- Docker
- VSCode + Dev Containers extension


## Running the Backend (devcontainer)

1. Press `Ctrl+Shift+P` → `Dev Containers: Reopen in Container`
2. Wait for the container build and setup to finish
3. The container automatically installs `requirements.txt` into the container Python environment
4. Start the server:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

If you do not use the Dev Container, install the dependencies with `pip install -r requirements.txt`.

## Running Tests

Tests use an SQLite in-memory database.

```bash
pytest
```

Test files are located in `backend/tests/`.

## Project Structure

```
backend/
  app.py          # FastAPI application and routes
  database.py     # SQLAlchemy engine reading DATABASE_URL from environment
  tests/
    conftest.py   # sets DATABASE_URL to SQLite in-memory for all tests
    test_smoke.py # smoke tests for core endpoints
pytest.ini        # pytest configuration
.env.example      # example environment variables
requirements.txt  # dependencies
```
