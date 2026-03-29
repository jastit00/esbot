# Quality Model – ESBot

## Why These Four?

The selection is driven by ESBot's nature as a chat-based, AI-powered learning assistant with external service dependencies, built in the context of a software testing course:

| # | Quality Aspect | Core Reason for Selection |
|---|---|---|
| 1 | **Usability** | Chat interface must work intuitively without any user training; the entire educational value depends on students being able to use it effectively from the first session |
| 2 | **Reliability** | ESBot depends on an external AI inference backend that can fail; graceful degradation and fault tolerance are critical to prevent loss of learning continuity |
| 3 | **Performance Efficiency** | Every user interaction triggers an external AI call; response times are directly visible to users, and the system must handle up to 50 concurrent users without degradation |
| 4 | **Maintainability** | ESBot is developed as a group project with parallel development across multiple components; evolving requirements such as adding new quiz types or swapping the AI provider make a modular, layered architecture essential to keep changes self-contained and the system extensible |

---

## Quality Model Structure (3-Step Approach)

Each quality aspect is modeled using the three-step method introduced in the lecture:

1. Abstract – General quality goal aligned to ISO 25010
2. Specific – Concrete interpretation within the ESBot problem domain
3. Measurable – Quantitative indicators and target values for verification

---

## 1. Usability

| Step | Content |
|---|---|
| **1. Abstract** | ESBot shall be usable by first-time users without any prior training or documentation. |
| **2. Specific** | A student unfamiliar with AI chat tools should be able to ask a content question, receive an explanation, and request a quiz within their first session without external help. The interface must clearly communicate available actions and guide the user when inputs are ambiguous. |
| **3. Measurable** | ≥ 80% of new test users complete a full learning interaction on first use unaided; time-to-first-meaningful-interaction ≤ 60 s; post-session satisfaction score ≥ 4/5. |

---

## 2. Reliability

| Step | Content |
|---|---|
| **1. Abstract** | ESBot shall remain functional and user-friendly even when external AI services are unavailable or return errors. |
| **2. Specific** | When the AI backend is unreachable or returns an error, ESBot shall display a meaningful fallback message (e.g., *"The AI service is temporarily unavailable — please try again shortly."*) rather than crashing. Session history shall not be lost due to transient failures. |
| **3. Measurable** | 100% of AI service failures produce a user-facing fallback message (zero unhandled exceptions exposed); system uptime ≥ 99% during scheduled usage; session data preserved across ≥ 95% of transient failures. |

---

## 3. Maintainability

| Step | Content |
|---|---|
| **1. Abstract** | ESBot shall follow a modular architecture that allows independent development, modification, and replacement of subsystems. |
| **2. Specific** | - The system must separate concerns across all layers of ESBot. <br> - Communication through well-defined interfaces. |
| **3. Measurable** | - Every feature change is reviewed in a Code Review, verifying that the change is self-contained and does not unintentionally affect other modules. <br> - After each change, the affected modules are tested (unit and/or integration tests) to ensure no regressions were introduced. <br> - All inter-module interfaces are documented before implementation and checked for completeness during Code Review. |

---

## 4. Performance Efficiency

| Step | Content |
|---|---|
| **1. Abstract** | ESBot shall respond to user queries within acceptable time limits under expected load conditions, making efficient use of backend and AI inference resources. |
| **2. Specific** | When a student sends a question, explanation request, or quiz prompt via the chat interface, the system shall deliver a complete response within 2–5 seconds under normal load (up to 50 concurrent users). The backend API and AI integration layer shall not hold unnecessary connections or block threads while awaiting AI responses. The system should support independent scaling of the AI inference component to handle load spikes. |
| **3. Measurable** | - End-to-end response time ≤ 5 s for ≥ 95% of requests under 50 concurrent users. <br> - System sustains ≥ 50 concurrent sessions without response time degradation beyond the 5 s threshold. |

---

## Testability Measures During Development

Specific measures we believe should be implemented during the development of ESBot to guarantee the quality aspect of "testability":

### 1. Specification-Driven Development (Spec-First)

Following the SDD principle introduced in the lecture, all API endpoints and component interfaces are specified before any implementation begins. Each specification item directly maps to one or more test cases, test design becomes a natural by-product of the specification rather than an afterthought.

### 2. Three-Level Test Strategy

The system is tested at three distinct levels to cover all layers of the application:

| Level | What is tested | AI Dependency |
|---|---|---|
| **Unit Tests** | Individual functions and classes in isolation (e.g. quiz logic, answer evaluation, session handling) | Fully mocked |
| **Integration Tests** | Interaction between components (API ↔ service ↔ database) | Mocked |
| **System Tests** | Full end-to-end flow from user request to response | Mocked via stub |

### 3. Separation of Concerns

Each layer of ESBot has a single, clearly defined responsibility and communicates only through well-defined interfaces. This ensures that every component, especially the AI inference client, can be replaced with a mock or stub during testing without modifying production code.

### 4. Automated Tests in CI Pipeline

All tests run automatically on every commit and merge request. The CI pipeline enforces a minimum code coverage threshold, executes the full test suite with the AI backend replaced by a mock, and fails the build if any test fails or coverage drops ensuring that testability is continuously maintained throughout the project lifecycle.
