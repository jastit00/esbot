# ESBot – Usecases

ESBot is a web-based AI learning assistant that helps students understand and practice course content through a guided conversational interface

![ucdiagram](https://github.com/jastit00/esbot/blob/assignment2/docs/spec/img/usecase.jpg)

## UseCase-001
### Title: 
Upload Learning Material
### Primary Actor:
Student

### Stakeholders and Interests:
Student: Wants to provide course material so ESBot can support learning based on that content

### Preconditions: 
- The student is authenticated and has access to ESBot
- The upload or input interface for material is available
- Enough storage is available

### Trigger:
The student chooses the option in ESBot to upload or provide learning material
  
### Main Success Scenario: 
1. Student opens ESBot and navigates to the “Upload Material” function
2. Student selects one or more files or pastes textual content
3. Student confirms the upload
4. System validates the input 
5. System stores the material in persistent storage
6. System associates the stored material with the student’s context or session
7. Student sees a confirmation message and possible next actions (summarize, ask questions, request test)

### Postconditions:
- The material is stored and linked to the student’s context
- ESBot can access this material for later summary, Q&A, and test generation
  
### Extensions (Alternate Flows): 
- 4a. Invalid or Unsupported Material:
  - 4a1. System detects unsupported file type, size limit exceeded, or unreadable content
  - 4a2. System informs the student and asks to adjust or choose different material
 
- 5a. Storage Failure:
  - 5a1. System cannot persist the material due to a technical error
  - 5a2. System informs the student that the upload failed and suggests retrying later
  
### Special Requirements: 
- Only supported file types and sizes may be accepted
- Stored material must be handled securely and associated with the correct user/session
  
### Frequency of Use: 
- Occasionally (a few times per session when new material is introduced)




## UseCase-002
### Title: 
Summarize Uploaded Material
### Primary Actor:
Student

### Stakeholders and Interests:
Student: Wants a concise summary of the material to quickly understand key points

### Preconditions: 
- The student has previously uploaded or provided at least one piece of material
- ESBot can access the stored material and an AI inference engine is configured or a fallback exists
  
### Trigger:
The student requests a summary of selected material via the UI or chat

### Main Success Scenario: 
1. Student selects the material to summarize or issues a summary request while a document is active
2. System identifies the corresponding stored material for the request
3. System retrieves the material from persistent storage
4. System constructs a prompt for the AI model including the material
5. System sends the prompt to the AI inference engine
6. AI returns a summary; system validates and structures it
7. System stores the generated summary and interaction in the session history
8. System presents the summary to the student in the interface

### Postconditions:
- A structured summary of the selected material is available to the student
- The summary and the request are stored as part of the learning session
  
### Extensions (Alternate Flows): 
- 2a. No Matching Material:
  - 2a1. System cannot find the referenced material
  - 2a2. System asks the student to choose from a list of available materials

- 5a. AI Inference Unavailable:
  - 5a1. System cannot contact the AI engine or receives an error
  - 5a2. System logs the failure and informs the student that summarization is temporarily unavailable

- 6a. Unusable AI Output:
  - 6a1. System detects that the AI output is malformed, empty, or clearly off-topic
  - 6a2. System retries once with an adjusted prompt or falls back to a simpler error or guidance message
  
### Special Requirements: 
- Response time for summary requests should  be within a few seconds 
  
### Frequency of Use: 
- Regularly




## UseCase-003
### Title: 
Ask Questions About Material
### Primary Actor:
Student

### Stakeholders and Interests:
Student: Wants clear, contextual explanations that directly refer to the selected material

### Preconditions: 
- The student has previously uploaded or provided at least one piece of material
- ESBot can access the stored material and an AI inference engine is configured or a fallback exists
  
### Trigger:
- The student submits a question related to the material via the ESBot chat interface

### Main Success Scenario: 
1. Student enters a natural-language question referring to the material 
2. System receives the question together with the current session or material context
3. System determines which material is relevant for the question
4. System retrieves the relevant material or portion from persistent storage
5. System constructs an AI prompt including the question and the relevant context from the material
6. System sends the prompt to the AI inference engine
7. AI returns an answer; system validates and structures it into a clear explanation
8. System stores the question and answer in the session history
9. System presents the explanation to the student within the chat interface

### Postconditions:
- The student receives an explanation that relates to the chosen material
- The question and answer are stored for later review and continued learning
  
### Extensions (Alternate Flows): 
- 3a. No Material Context Determined:
  - 3a1. System cannot clearly determine which material the question refers to
  - 3a2. System asks the student to choose or confirm the relevant material

- 4a. Material Retrieval Fails:
  - 4a1. System cannot retrieve the material from storage
  - 4a2. System informs the student and suggests retrying or re-uploading the material

- 6a. AI Inference Fails:
  - 6a1. System cannot obtain a response from the AI engine
  - 6a2. System logs the error and provides a fallback message to the student

- 7a. Answer Off-topic or Unclear:
  - 7a1. System detects that the answer is clearly unrelated or unusable
  - 7a2. System retries once with an improved prompt or informs the student that a suitable explanation cannot be generated
  
### Special Requirements: 
- Explanations should remain comprehensible and focused on the material, avoiding irrelevant digressions
- The system should support storing Q&A interactions to allow students to revisit prior explanations
  
### Frequency of Use: 
- Frequently (main function of the System)




## UseCase-004
### Title: 
Generate Test for Material
### Primary Actor:
Student

### Stakeholders and Interests:
Student: Wants a quiz or test based on the material to practice and assess understanding

### Preconditions: 
- The student has uploaded material suitable for question generation
- ESBot can access the material and an AI inference engine is available or a fallback strategy is defined
  
### Trigger:
- The student requests a test or quiz based on specific material

### Main Success Scenario: 
1. Student selects the option to generate a test for selected material or requests it via chat
2. System confirms or determines which material is the basis for the test
3. System retrieves the material from persistent storage
4. System constructs a prompt instructing the AI to generate a set of questions (and optionally answers) based on the material
5. System sends the prompt to the AI inference engine
6. AI returns a list of questions (and possibly suggested answers or solution notes)
7. System validates and structures the questions into a quiz format
8. System stores the generated quiz and any reference answers in the student’s session
9. System presents the quiz to the student in the interface for completion

### Postconditions:
- A test or quiz based on the selected material is available in ESBot for the student to work on
  
### Extensions (Alternate Flows): 
- 2a. No Suitable Material Selected:
  - 2a1. System cannot find or confirm material for test generation
  - 2a2. System asks the student to choose from a list of available materials

- 3a. Material Not Suitable:
  - 3a1. System determines that the material is too short, too long, or not suitable for meaningful question generation
  - 3a2. System informs the student and may suggest different material or a reduced scope

- 5a. AI Inference Unavailable:
  - 5a1. System cannot obtain questions from the AI engine
  - 5a2. System logs the failure and informs the student that test generation is temporarily unavailable

- 6a. Generated Questions Are Invalid:
  - 6a1. System detects malformed or clearly irrelevant questions
  - 6a2. System retries generation with adjusted instructions or informs the student that a suitable quiz cannot be generated
  
### Special Requirements: 
- The system should support later evaluation of student answers, at least with basic correctness feedback
  
### Frequency of Use: 
- occasionally

_Perplexity AI was used to support with formulating the use-case descriptions_
