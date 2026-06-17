# Manual UI Test Report

**Date:** 17.06.2026
**Tester:** Vincent Kehl 
**OS:** Windows 11  
**Browser:** Firefox  
**LLM:** MockAIInference 

---

## TC-UI-01 - Create a New Session

| | |
|---|---|
| Steps | Click + New Session |
| Expected | Session appears in list, chat panel opens |
| Actual | Session appeared, chat panel opened |
| Result | **Pass** |

---

## TC-UI-02 - Send a Chat Message


| | |
|---|---|
| Steps | Select session -> type message -> click Send |
| Expected | User message and ESBot answer appear |
| Actual | Both appeared with mock response |
| Result | **Pass** |

---

## TC-UI-03 - Generate a Quiz

| | |
|---|---|
| Steps | Switch to Quiz tab -> enter topic -> click Generate Quiz |
| Expected | Question appears with 4 answer options |
| Actual | Two mock questions generated, 4 answer options visible |
| Result | **Pass** |

---

## Reflection

All three tests worked as expected. Testing by hand was simple but slow. Automated tests would do the same checks faster and run on every code change.
