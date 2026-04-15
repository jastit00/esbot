# ESBot Data Model

## Scope
This document defines the core persistence model for ESBot. The goal is a minimal but complete relational model that supports learning sessions, chat messages, quiz generation, submitted answers, and answer evaluation.

## Final Entity List
The selected core entities are:

- `UserSession`
- `Message`
- `QuizRequest`
- `QuizItem`
- `SubmittedAnswer`
- `EvaluationResult`

## Persistence Mapping Strategy
ESBot uses a relational persistence model mapped to PostgreSQL via SQLModel/SQLAlchemy.

- Each entity is mapped to its own table.
- Foreign keys are used to represent ownership and dependency between records.
- Bidirectional ORM relationships are used for navigation in Python code.
- Timestamps are stored as timezone-aware UTC datetimes.

## Relationship Cardinalities

- `UserSession` 1 - n `Message`
- `UserSession` 1 - n `QuizRequest`
- `UserSession` 1 - n `QuizItem`
- `UserSession` 1 - n `SubmittedAnswer`
- `QuizRequest` 1 - n `QuizItem`
- `QuizItem` 1 - n `SubmittedAnswer`
- `SubmittedAnswer` 1 - 1 `EvaluationResult`

## Attribute Notes

- Primary keys are integer IDs.
- Required text fields are validated with non-empty constraints in the model layer.
- `created_at` is generated automatically in UTC.
- `EvaluationResult.is_correct` stores the evaluation outcome as a boolean.

## Entity Relationship Diagram

![erdiagram](https://github.com/jastit00/esbot/blob/assignment4/docs/spec/img/ESbotER.png)

## Design Rationale
The model is intentionally compact and focuses on the minimum set of entities needed for the ESBot baseline. It captures conversation history, quiz lifecycle, user responses, and evaluation feedback without introducing extra abstraction layers or denormalized storage.

This model is suitable for PostgreSQL and keeps the persistence layer easy to test, reason about, and extend later if more detailed learning analytics or richer content types are introduced.
