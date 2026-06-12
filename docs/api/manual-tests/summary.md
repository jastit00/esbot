# ESBot API – Manual Test Summary

 
All tests returned the expected error code, the messages api is not useful because there is no endpoint for message creation implemented. The error codes provide enough feedback to pinpoint the underlying errors

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

## GET /api/v1/sessions/{session_id}/messages 

![get messages error](./get_messages_error.png)

---

## DELETE /api/v1/sessions/{session_id}

![delete session](./delete_session.png)

---



![delete session error](./delete_session_error.png)
