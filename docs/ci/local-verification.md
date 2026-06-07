# Local Verification (Exercise 9.1, Phase A)

This document records the exact commands that prove "ESBot is healthy" on a
local machine. The CI workflow (`.github/workflows/ci.yml`) MUST run the same
commands (or a documented subset).

## Stack

- **Language / runtime:** Python 3.11
- **Web framework:** FastAPI
- **ORM:** SQLModel
- **Tests:** pytest (+ behave for BDD)
- **Linter:** pylint

## Prerequisites

Install dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
python -m pip install pylint
```

For tests no live LLM inference engine is required — the AI engine is mocked
via `MockAIInference` (see `backend/services/question_service.py`, introduced
in Exercise 8).

The database is configured per environment variable `DATABASE_URL`. For local
verification and CI we use a file-based SQLite database, which keeps the test
suite hermetic and requires no external service.

## A.1 — Run the test suite

From the repository root:

```bash
DATABASE_URL="sqlite:///./test.db" python -m pytest
```

Expected result: **61 passed** (status as of 2026-06-07).

Notes:
- The `pytest.ini` already pins `testpaths = backend/tests` and
  `pythonpath = .`, so no extra flags are required.
- BDD scenarios can additionally be executed via
  `behave backend/tests/features/` (see `Makefile`).
- No flaky tests are currently known. Should one appear, fix it or mark it
  with `@pytest.mark.skip(reason="…")` and add an entry below.

### Known skipped / waived tests

_None at the moment._

## A.2 — Run static analysis

From the repository root:

```bash
python -m pylint backend/
```

Current score: **6.65 / 10** (2026-06-07).

Pylint findings are intentionally non-blocking for now; remaining issues are
tracked in [docs/spec/static-analysis.md](../spec/static-analysis.md).
To run pylint without failing the shell (useful for first CI run), append
`--exit-zero`:

```bash
python -m pylint backend/ --exit-zero
```

## Quick reference

| Step | Command                                                       |
|------|---------------------------------------------------------------|
| A.1  | `DATABASE_URL="sqlite:///./test.db" python -m pytest`         |
| A.2  | `python -m pylint backend/`                                   |

These two commands together form the local verification gate that the CI
workflow will replicate in Phase B.

---

<!--
Tool Used: Claude Opus 4.7
Purpose: Wurde ausschliesslich zur Formulierungs- und Struktur-Unterstuetzung
         (z. B. korrekte Markdown-Tabellen, einheitliche Formatierung der
         Befehls-Snippets) eingesetzt.
         Die KI diente lediglich als unterstuetzendes Hilfsmittel und nicht als
         primaere Quelle der Loesung.
-->

