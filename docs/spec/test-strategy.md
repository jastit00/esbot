# Test Strategy

## Differences between unit tests and BDD/acceptance tests

### Unit Tests

| Aspect | Description |
|--------|-------------|
| **Execution Time** | Fast (milliseconds to seconds per test) |
| **Scope** | Testing individual components (functions, methods, classes) in isolation |
| **Purpose** | Ensure code precision at micro-level (logical correctness of individual units) |
| **Goal** | Test implementation |
| **Written in** | Same language as the code under test |


### BDD/Acceptance Tests

| Aspect | Description |
|--------|-------------|
| **Execution Time** | Slower (seconds to minutes per scenario) |
| **Scope** | Testing whole system from user's perspective (system interactions, workflows) |
| **Purpose** | Ensure the system behaves as expected from a user's perspective |
| **Goal** | Test behavior |
| **Written in** | Gherkin Syntax (natural language) |

---

## Execution Frequency of Tests

As seen in the tables above unit tests and BDD/Acceptance Tests are very different in their execution time, scope, and purpose. Therefore it's normally not recommended to run them always together.

**Unit Tests** can be run on every commit due to their fast execution time, easy error handling, fast feedback, and small scope.

**BDD/Acceptance Tests** should be run on a scheduled basis or on pull requests due to slower execution time, broader scope, and more complex setup. Additionally the workflows don't change that often, so running these test on every commit is not necessary.

### Recommendation for ESBot:
- Run all Unit Tests on every commit.
- Run BDD/Acceptance Tests on every pull request.

---

## Impact of AI Mockability

- **Deterministic Output**: Mock AI makes tests repeatable, because responses are predictable
- **Execution Time**: Mock AI brings faster execution, eliminating network latency or AI inference time
- **Dependencies**: Mock AI eliminates external API dependencies (API availability or rate limits)
- **Controlled Scenarios**: With mock AI edge cases that would be difficult to reproduce with real AI are easily testable

Without Mock AI even BDD/Acceptance tests on pull requests would be problematic due to slowness, dependency on external API and loss of control over AI results.

---

*Tool Used: Windsurf Tab Completion*
*Purpose: Autocompletion of md-Syntax, help with wording and spelling correction*