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

### Trigger:
The student chooses the option in ESBot to upload or provide learning material

### Preconditions: 
- The student is authenticated and has access to ESBot
- The upload or input interface for material is available
- Enough sotrage is available
  
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
  
### Special Requirements: 
- Only supported file types and sizes may be accepted
- Stored material must be handled securely and associated with the correct user/session
  
### Frequency of Use: 
- Occasionally (a few times per session when new material is introduced)

