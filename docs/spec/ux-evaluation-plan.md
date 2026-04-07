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
 
## Method set
- Questionnaire: Perform a Questionnaire based on the user experience questionnaire (UEQ) and system usability scale (SUS)
- Heuristic Evaluation: Perform an Evaluation against Nielsens 10 Usability Heuristics
- Cognitive Walkthrough: Perform a Cognitive Walkthrough for User Journeys
- Expert Sample Review: Check ESBot for quality and correctness of responses

## Participants and setup
 ### Participants
  | User | Experience | Amount | Reasoning
  |-----|------|---------|----------|
  First-time users | No prior ESBot experience | 5 | Perform Questionnaires and Heuristic Evaluation
  Usability Experts | Expertise in UX | 3 | Perform Heuristic Evaluation and Cognitive Walkthroughs
  Domain Expert | Expertise in Specific Domain | 1 | Perform Expert Sample Review
  
 ### Session duration
  - 45–60 minutes per user session; 60–90 minutes for heuristic + walkthrough sessions.
  - 15 min for expert sample review
  
 ### Materials
  - Running ESBot Application
  - SUS + UEQ questionnaire
  - Finding Templates
  - Screenshot tool
  
## Metrics and acceptance criteria
| # | UX Factors               | Metric                                                        | Acceptance Threshold | ISO 25010 Mapping                                                          | Verification Method                                                           |
| - | ------------------------ | ------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------- | ---------------------------------------- |
| 1 | Intuitive Operation      | Task completion rate (first-time users, no assistance)        | ≥ 90%                | Usability: Appropriateness Recognizability, Learnability                   | Cognitive Walkthrough                 |
| 2 | Helpfulness / Efficiency | Users answering follow-up questions correctly after ESBot use | ≥ 85%                | Functional Suitability: Functional Appropriateness, Usability: Operability | UEQ (efficiency + usefulness) |
| 3 | Ease of Use              | SUS Score (mean across participants)                          | ≥ 80                 | Usability: Operability, User Error Protection                              | SUS questionnaire post-session                                                |
| 4 | Correctness              | Responses rated correct by domain expert review               | ≥ 95%                | Functional Suitability: Functional Correctness, Reliability: Maturity      | Expert Sample Review (correct / minor error / critical error)                 |
| 5 | Controllability          | Identical inputs producing consistent outputs                 | ≥ 99%                | Usability: Operability, Reliability: Recoverability                        | Repeated input testing                                                        |

## Findings template

- Finding ID: Unique ID to identify issue
- Title: Short specific description
- Description: Description of the issue, in what context or user journey it occured, and what UX Factors are affected
- Severity: Divided into four levels, critical(task failure, journey could not be completed), high(factor doesnt reach acceptance threshold), medium(factor only barely reaches acceptance threshold), low(cosmetic issues)
- Evidence: Material, e.g Screenshots
- Recommendation: proposal for issue mitigation
- Status: Status of issue (new, in progress, under evaluation, fixed)

## Quality gate proposal

Define when UX issues block a release:
- Any finding with the severity "critical" exists without the status "fixed"
- There is more then one finding with the severity "high" without the status "fixed"
- There is more then one finding with the severity "medium" without the status "fixed" or "under evaluation" or "in progress"





