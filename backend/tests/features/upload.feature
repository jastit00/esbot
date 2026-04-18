Feature: Upload Learning Material
    As a student
    i want to upload learning Material
    so that EsBot can use it for Interactions

Scenario: Sucessful Upload
    Given the student has access to the running EsBot
    When the student navigates to "Upload Material" 
    And the student selects one or more files 
    And the student confirms the upload
    Then the system validates the input
    And the system stores the material in persistent storage
    And the system links the material to the student context
    And the student sees a confirmation message
    And the student is offered next actions like "summarize", "ask questions", or "request test"

Scenario: Upload fails due to invalid or unsupported material
    Given the student has access to the running EsBot
    When the student navigates to "Upload Material"
    And the student selects an unsupported file type or oversized file or unreadable content
    And the student confirms the upload
    Then the system detects invalid input
    And the system informs the student about the issue
    And the system asks the student to adjust or upload different material

 Scenario: Upload fails due to storage error
    Given the student has access to the running EsBot
    When the student navigates to "Upload Material"
    And the student selects valid material
    And the student confirms the upload
    But the system cannot store the material due to not enough storage being available
    Then the system informs the student that the upload failed
    And the system suggests retrying later and informing an administrator