## Exercise 10.3 (test_endpoints.py)

### Framework choice

`pytest` + `FastAPI TestClient` because it's simple and we have FastAPI as our framework.


### How to run the suite

```bash
# In devcontainer (/workspace)
pytest /workspace/backend/tests/api/test_endpoints.py
```


### How the backend is started for tests

The backend is stared using a devcontainer (config in our repo). With the devcontainer started and workspace opened in it, the above command can be executed to run all tests without an error.


### Description of each test group

`test_health_endpoint()`: Tests to endpoint to ensure the API is running.

`test_session_creation()`: Tests the creation of a new session.

`test_session_listing()`: Tests the listing of all exisiting sessions.

`test_message_history_retrieval()`: Tests getting all messages for a given session.

`test_session_deletion()`: Tests deleting a session.

---

`test_session_not_found()`: Tests getting a session that does not exist.

`test_session_get_no_messages()`: Tests getting all messages of a session that has no messages.

`test_non_exisiting_session_deletion()`: Tests deleting a session that does not exist.

`test_invalid_session_id_format()`: Tests getting a session with an invalid format of the session id.



---
**Tool Used:** Windsurf Tab Completion

**Purpose:** Wurde nur eingesetzt um die Syntax zu vervollständigen (Sätze zu vervollständigen).