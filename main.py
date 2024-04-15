from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def run(UCInetID, password, presenter_code, wait_time=60*60*2):
    pollev_url = "https://pollev.com/login"

    with webdriver.Chrome() as driver:
        try:
            # Navigate to the login page
            driver.get(pollev_url)

            # Log in using the organization-specific method
            login_with_organization(driver, UCInetID, password, 10)

            time.sleep(5)

            # Join using a presenter's code
            join_presenter_by_code(driver, presenter_code, 10)

            time.sleep(5)

            # Interact with the session options
            select_first_option(driver, wait_time)

            # Refresh the page to ensure updates are fetched
            driver.refresh()

        except Exception as e:
            print(f"Error during processing: {e}")

        finally:
            input("Press Enter to quit")

def login_with_organization(driver, UCInetID, password, wait_time):
    """Completes user login through the organization's authentication page."""
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, 'username'))
    ).send_keys(UCInetID + "@uci.edu")

    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.NAME, 'button'))
    ).click()

    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, "//button[span[text()='Log in with UCI']]"))
    ).click()

    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, 'j_username'))
    ).send_keys(UCInetID)

    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, 'j_password'))
    ).send_keys(password)

    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.NAME, 'submit_form'))
    ).click()

def join_presenter_by_code(driver, code, wait_time):
    """Enters the presenter's code to join the session."""
    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.ID, 'participate_home_form_presenter'))
    ).send_keys(code)

    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.NAME, 'button'))
    ).click()

def select_first_option(driver, wait_time):
    """Selects the first multiple-choice option available."""
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".component-response-multiple-choice__option__vote"))
    ).click()

if __name__ == "__main__":
    UCInetID = "petergriffin"
    password = "114514"
    present_code = "quagmire711"
    run(UCInetID, password, present_code)