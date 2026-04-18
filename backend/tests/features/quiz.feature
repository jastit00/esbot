Feature: Generate Test for Learning Material
    As a student
    I want to generate a test based on my material
    So that I can practice and assess my understanding


  Scenario: Successful test generation
    Given the student has access to the running EsBot
    And the student has previously uploaded at least one material
    When the student requests a test for selected material
    Then the system determines the relevant material
    And the system evaluates the selected material
    And the system retrieves the material from storage
    And the system constructs a prompt for question generation
    And the system sends the prompt to the AI engine
    And the system receives a list of questions
    And the system validates and structures the quiz
    And the system stores the quiz in the student session
    And the system presents the quiz to the student

  Scenario: No suitable material selected
    Given the student has access to the running EsBot
    And the student has previously uploaded at least one material
    When the student requests a test for selected material
    And the system cannot determine relevant material
    Then the system asks the student to choose from available materials

  Scenario: Material not suitable for test generation
    Given the student has access to the running EsBot
    And the student has previously uploaded at least one material
    When the student requests a test for selected material
    Then the system determines the relevant material
    When the system evaluates the selected material
    And the material is too short or too long or unsuitable
    Then the system informs the student about the issue
    And the system suggests alternative material or reduced scope

