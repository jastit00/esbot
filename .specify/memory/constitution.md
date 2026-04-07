# ESBot Constitution

## Core Principles

### I. Strict Layer Separation
All features MUST preserve strict 3-tier separation between UI, Backend, and Database, with the
LLM treated as an external service accessed by the backend only. UI code MUST handle presentation
and user interaction only. Backend code MUST own business logic, orchestration, validation,
logging, and all external integrations. Database code MUST remain behind backend-managed
persistence boundaries. Mixed-layer modules and direct UI-to-database communication are prohibited.

Rationale: Clear boundaries keep the system understandable, testable, and easier to evolve
without hidden coupling.

### II. Backend-Owned LLM Access
The LLM MUST be accessible only through backend-owned interfaces. Frontend clients MUST NEVER call
an LLM provider directly. Backend integrations MUST isolate prompts, provider configuration,
fallback handling, and response normalization behind modular adapter components that can be
replaced without changing UI or persistence layers.

Rationale: Centralizing AI access protects credentials, contains non-deterministic behavior, and
keeps provider changes from spreading across the codebase.

### III. REST Contract Consistency
Frontend-backend communication MUST use REST only. Every endpoint MUST define consistent request
and response schemas, perform input validation before executing business logic, and return
documented error responses. Contract changes MUST update both schemas and tests before merge.

Rationale: Stable REST contracts reduce integration failures and make frontend and backend work
independently maintainable.

### IV. Mandatory Persistence
All sessions and messages MUST be persisted; stateless operation is not allowed. Features that
create, update, summarize, or present conversations MUST use backend-managed persistence
components and durable storage. Data access patterns MUST preserve conversation continuity and
support reliable retrieval of prior interactions.

Rationale: Persistent state is a core product behavior and essential for continuity across
learning sessions.

### V. Testability and Observability
Core logic MUST have unit tests. API and database behavior MUST have integration tests. Automated
tests covering AI-enabled flows MUST use mocked, stubbed, or fake LLM behavior and MUST NOT make
real AI calls. Major actions and error paths MUST be logged with enough context to diagnose
failures without mixing responsibilities across layers. Components such as API handlers,
repositories, and LLM adapters MUST remain modular and replaceable.

Rationale: ESBot must be easy to verify, debug, and extend in a controlled way.

## Architecture Standards

- The approved interaction path is `UI -> Backend -> Database`, with `Backend -> LLM` as an
  external service call when AI behavior is required.
- Frontend code MUST communicate with the backend through REST endpoints only.
- Backend code MUST own validation, orchestration, persistence access, and LLM access.
- Database interactions MUST be encapsulated behind backend-owned repository or persistence
  components.
- Components that wrap the LLM, database, or transport layer MUST be replaceable without changing
  unrelated layers.

## Delivery Workflow

- Plans MUST include a constitution check covering layer separation, backend-only LLM access,
  REST-only communication, persistence impact, validation, logging, and required tests.
- Specifications MUST document affected REST contracts, persistence behavior, validation rules,
  logging expectations, and the LLM mocking approach when a feature touches those areas.
- Tasks MUST include work for unit tests, integration tests, endpoint validation, logging, and
  persistence changes whenever applicable.
- Reviews MUST reject changes that bypass the backend for AI access, mix layers, skip persistence
  for sessions or messages, omit input validation, or leave required tests uncovered.

## Governance
This constitution governs project planning, implementation, and review. Amendments MUST document
the affected principles, explain the operational impact, and update dependent templates in the
same change whenever possible. Versioning follows semantic rules: MAJOR for incompatible
governance changes or principle removals, MINOR for new principles or materially expanded rules,
and PATCH for clarifications that do not change expectations. Compliance MUST be checked in
implementation plans, task generation, code review, and release-readiness review.

**Version**: 1.0.0 | **Ratified**: 2026-03-29 | **Last Amended**: 2026-03-29
