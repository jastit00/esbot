# ESBot API – Manual Test Summary

 Findings:
- All tests returned the expected error code.
- the messages api is not useful because there is no endpoint for message creation implemented.
- The error codes provide enough feedback to pinpoint the underlying errors

---

## GET /api/v1/health

![health check](./healthcheck.png)

---

## POST /api/v1/sessions

![create session](./create_session.png)

---

## GET /api/v1/sessions

![list sessions](./get_sessions.png)

---

## GET /api/v1/sessions/{session_id}/messages

![get messages](./get_messages.png)

---

## DELETE /api/v1/sessions/{session_id}

![delete session](./delete_session.png)

---

## DELETE /api/v1/sessions/{session_id} for non-existing session

![delete session error](./delete_session_error.png)

---
## GET /api/v1/sessions/{session_id}/messages for non-existing session

![get messages error](./get_messages_error.png)

---
