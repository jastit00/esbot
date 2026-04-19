# Backend

## Tech Stack

| Concern | Choice |
|---|---|
| Framework | FastAPI |
| ASGI server | uvicorn |
| ORM / persistence | SQLModel |
| Database (production) | PostgreSQL |
| Database (tests) | SQLite in-memory |
| Test framework | pytest |

## Prerequisites

- Docker
- VSCode + Dev Containers extension

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://esbot_user:esbot_password@db:5432/esbot` |

The devcontainer sets `DATABASE_URL` automatically via `docker-compose.yml`. No manual configuration needed.

## Running the Backend (devcontainer)

1. Press `Ctrl+Shift+P` → `Dev Containers: Reopen in Container`
2. Wait for the container build and setup to finish
3. Start the server:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`. Database tables are created automatically on startup.

## Running Tests

Tests use an SQLite in-memory database: no running PostgreSQL instance required.

**Unit tests only:**
```bash
pytest
```

**BDD acceptance tests only:**
```bash
behave backend/tests/features/
```

**Full test suite (unit + BDD):**
```bash
make test
```

Test files are located in `backend/tests/`.

## Verifying the Database

After starting the server, verify PostgreSQL tables were created correctly via (execute locally):

```bash
docker exec -it esbot-db psql -U esbot_user -d esbot -c "\dt"
```

## Project Structure

```
backend/
├── app.py           # FastAPI application, lifespan, and routes
├── database.py      # SQLModel engine and session
├── models.py        # SQLModel table definitions
└── tests/
    ├── conftest.py          # session and client fixtures with SQLite in-memory DB
    ├── test_smoke.py        # smoke test for the root endpoint
    └── test_session.py      # unit tests for Session entity
pytest.ini           # pytest configuration
requirements.txt     # dependencies
.devcontainer/
├── devcontainer.json    # VSCode dev container configuration
└── docker-compose.yml   # app + PostgreSQL services
```
