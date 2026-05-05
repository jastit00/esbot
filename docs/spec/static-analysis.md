## 1) Categories and tools


**Security (Bandit):** Bandit detects common security issues in Python code, such as unsafe function usage or insecure patterns, with minimal setup. This is important for ESBot since it processes user input and interacts with external systems.

**Maintainability (Pylint):** Pylint identifies issues like unused imports, undefined variables, and overly broad exception handling early. This helps maintain code quality and reduces the risk of bugs, especially in a growing codebase with multiple components.

---
## 2) Configuration

Both tools were installed locally using pip and configured with minimal changes from their default settings.

Pylint configuration:
- `missing-docstring` is disabled since documentation is not yet consistently maintained while the codebase is still evolving  
- `too-few-public-methods` is disabled because it is frequently triggered by Pydantic models that intentionally have only a few methods  
- `backend/tests/features` is excluded via `ignore-paths` since Pylint does not handle Behave decorator patterns correctly

Bandit is run with `-x backend/tests` to skip test files.

---
## 3) Running the Tools

Both are available as Makefile targets:

```bash
make lint       # runs: pylint backend/
make security   # runs: bandit -r backend/ -x backend/tests
```

---
## 4) Evaluation

**Pylint** (score: 6.97/10) highlights a few real issues in the application code, such as a shadowed `app` variable, an unused import, and the use of broad `Exception` handling in `question_service.py`. These are worth fixing. Most other warnings come from test files or from false positives, especially related to Pydantic (`model_fields`), which Pylint does not fully understand. This shows that Pylint is useful for catching real issues early, but it also produces a noticeable amount of noise due to non-critical warnings and framework-related false positives.

**Bandit** reports no issues in the application code, which suggests there are currently no obvious security problems such as hardcoded secrets or unsafe operations. It provides focused results with little noise.

Both tools run in a few seconds and do not slow down development. At this stage, they are used locally only. Pylint would require further tuning to reduce noise before being used as a strict CI check, and Bandit would benefit from a baseline to track changes over time.