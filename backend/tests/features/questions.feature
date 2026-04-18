Feature: Ask Questions About Learning Material
  As a student
  I want to ask questions about my uploaded material
  So that I receive clear, contextual explanations

  Scenario: Successful question answering with relevant material
    Given the student has previously uploaded at least one material
    When the student submits a question about the material
    Then the system receives the question with the current context
    And the system determines the relevant material
    And the system retrieves the relevant content from storage
    And the system constructs an AI prompt with question and context
    And the system sends the prompt to the AI engine
    And the system receives an answer
    And the system validates and structures the answer
    And the system stores the question and answer in session history
    And the system displays the explanation in the chat interface

  Scenario: Material retrieval fails
    Given the student has previously uploaded at least one material
    When the student submits a question about the material
    Then the system receives the question with the current context
    And the system identifies the relevant material
    But the system cannot retrieve the material from storage
    Then the system informs the student about the failure
    And the system suggests retrying or re-uploading the material

  Scenario: AI answer is off-topic or unclear
    Given the student has previously uploaded at least one material
    When the student submits a question about the material
    Then the system receives the question with the current context
    And the system determines the relevant material
    And the system retrieves the relevant content from storage
    And the system constructs an AI prompt with question and context
    And the system sends the prompt to the AI engine
    When the system receives an answer from the AI engine
    And the answer is detected as off-topic or unusable
    Then the system retries once with an improved prompt
    When the system fails with the improved prompt
    Then the system informs the student that no suitable explanation can be generated