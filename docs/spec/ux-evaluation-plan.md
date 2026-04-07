# UX Evaluation Plan

## Evaluation Scope
- UX Factors
  - Intuitive Operation
  - Helpfulness and Efficiency
  - Ease of Use
  - Correctness
  - Controllability
    
- User Journeys
  - Getting started with ESBot: Open the application for the first time, explore what the chatbot can do, and ask it a question of your choice.
  - Learning with own Material: Upload study material, request summary, ask 2-3 questions regarding the material
  - Trying a Quiz: Upload study material, ask ESBot to create a quiz, answer the questions
 
# Method set
Questionnaire: Perform a Questionnaire on the basis of the user experience questionnaire (UEQ) and system usability scale (SUS)
Heuristic Evaluation: Perform an Evaluation against Nielsens 10 Usability Heuristics
Cognitive Walkthrough: Perform a Cognitive Walkthrough for User Journeys

# Participants and setup
 ## Participants
  | User | Experience | Amount | Reasoning
  |-----|------|---------|----------|
  First-time users | No prior ESBot experience | 5 | Perform Questionnaires and Heuristic Evaluation
  Usability Experts | Domain-familiar | 3 | Perform Heuristic Evaluation and Cognitive Walkthroughs
  
## Session duration
  - 45–60 minutes per user session; 60–90 minutes for heuristic + walkthrough sessions.
  
## Materials
  - Running ESBot Application
  - SUS + UEQ questionnaire
  - Finding Templates
  - Screenshot tool
  
# Metrics and acceptance criteria
| # | Quality Goal             | Metric                                                        | Acceptance Threshold | ISO 25010 Mapping                                                          | Verification Method                                                           |
| - | ------------------------ | ------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 1 | Intuitive Operation      | Task completion rate (first-time users, no assistance)        | ≥ 90%                | Usability: Appropriateness Recognizability, Learnability                   | Think-aloud sessions, Cognitive Walkthrough                                   |
| 2 | Helpfulness / Efficiency | Users answering follow-up questions correctly after ESBot use | ≥ 85%                | Functional Suitability: Functional Appropriateness, Usability: Operability | Controlled experiment vs. traditional learning, UEQ (efficiency + usefulness) |
| 3 | Ease of Use              | SUS Score (mean across participants)                          | ≥ 80                 | Usability: Operability, User Error Protection                              | SUS questionnaire post-session                                                |
| 4 | Correctness              | Responses rated correct by domain expert review               | ≥ 95%                | Functional Suitability: Functional Correctness, Reliability: Maturity      | Expert sample review (correct / minor error / critical error)                 |
| 5 | Controllability          | Identical inputs producing consistent outputs                 | ≥ 99%                | Usability: Operability, Reliability: Recoverability                        | Repeated input testing                                                        |

# Findings template

- Finding ID: 
- Title: Short specific description
- Description: Description of the issue and in what context or user journey it occured
- Severity: Divided into four levels, critical(task failure), high(frustrating but with workaround), medium(), low(cosmetic issues)
- Evidence: Material, e.g Screenshots
- Recommendation: proposal for issue mitigation
- Status: Status of issue (new, in progress, fixed)

# Quality gate proposal





