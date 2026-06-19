"""
Prerequisites:
- Backend on http://localhost:8000
- Frontend on http://localhost:5173
- Chrome browser installed
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_chat_message(driver):
    """Create session and send chat message."""
    wait = WebDriverWait(driver, 15)

    # Wait for health status to be hidden (backend connected)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="health-status"]')))

    driver.find_element(By.CSS_SELECTOR, '[data-testid="new-session-btn"]').click()

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, '[data-testid="session-list"] li')) >= 1)

    message_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="message-input"]')
    message_input.send_keys("What are the first 100 decimal places of the square root of two?")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="send-message-btn"]').click()
    
    answer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="assistant-message"]')))
    assert "contextual explanation" in answer.text


def test_quiz_generation(driver):
    """Create a quiz and sumbit answers."""
    wait = WebDriverWait(driver, 15)

    # Wait for health status to be hidden (backend connected)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="health-status"]')))

    driver.find_element(By.CSS_SELECTOR, '[data-testid="new-session-btn"]').click()
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, '[data-testid="session-list"] li')) >= 1)

    quiz_tab = driver.find_element(By.CSS_SELECTOR, '[data-testid="quiz-tab"]')
    quiz_tab.click()
    quiz_topic = driver.find_element(By.CSS_SELECTOR, '[data-testid="quiz-topic-input"]')
    quiz_topic.send_keys("What are the first 100 decimal places of the square root of two?")
    driver.find_element(By.CSS_SELECTOR, '[data-testid="generate-quiz-btn"]').click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="quiz-question"]')))

    option_a = driver.find_element(By.CSS_SELECTOR, '[data-testid="quiz-option-0"]')
    option_a.click()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-answer-btn"]').click()

    option_b = driver.find_element(By.CSS_SELECTOR, '[data-testid="quiz-option-1"]')
    option_b.click()
    driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-answer-btn"]').click()

    feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="quiz-feedback"]')))
    assert "Quiz completed!" in feedback.text


def test_too_long_user_id_error(driver):
    """Create a session with a very long user ID to get an error."""
    wait = WebDriverWait(driver, 15)

    # Wait for health status to be hidden (backend connected)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="health-status"]')))
    
    user_id_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="user-id-input"]')
    user_id_input.send_keys("a" * 20000)
    driver.find_element(By.CSS_SELECTOR, '[data-testid="new-session-btn"]').click()

    error_banner = driver.find_element(By.CSS_SELECTOR, '[data-testid="error-banner"]')
    assert error_banner is not None
    # Verify that the server responded with HTTP 431 (Request Header Fields Too Large)
    #response = driver.execute_script("return window.performance.getEntriesByType('navigation')[0]")
    #print(response)
    #assert response["responseStatus"] == 431


"""
Tool Used: SWE-1.6 Slow, Windsurf Tab Completion
Purpose: SWE wurde als Starthilfe eingesetzt, um zu verstehen, wie man startet, was ein gutes negatives Scenario wäre und bei Fehlerbehebungen.
         Außerdem wurde der Response-Command in der letzten Funktion mithilfe von SWE generiert
"""