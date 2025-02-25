import os
import time
import math
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()

LOGIN = os.getenv("LOGIN") or "login"
PASSWORD = os.getenv("PASSWORD") or "password"

# links = ["https://stepik.org/lesson/236896/step/1"]
links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1", 
         "https://stepik.org/lesson/236897/step/1", 
         "https://stepik.org/lesson/236898/step/1", 
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1", 
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="session")
def collected_results():
    results = []
    yield results
    print("\nРезультаты всех тестов:")
    for result in results:
        print(result)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('site_link', links)
def test_guest_should_see_login_link(browser, site_link):

    link = f"{site_link}"
    browser.get(link)

    button_auth = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "navbar__auth")))
    button_auth.click()

    input_name = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']")))
    input_name.send_keys(f"{LOGIN}")

    input_pass = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    input_pass.send_keys(f"{PASSWORD}")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
    textarea_free = browser.find_element(
        By.CLASS_NAME, "quiz-component"
    ).get_attribute("data-state")
    if textarea_free != "correct":
        input_textarea = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")

        answer = math.log(int(time.time()))
        input_textarea.send_keys(answer)
        time.sleep(3)
        input_textarea = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")
        answer = math.log(int(time.time()))
        input_textarea.send_keys(answer)
        button_smb = browser.find_element(
            By.CSS_SELECTOR, "button.submit-submission"
        )
        button_smb.click()
        # print("После нажатия")
        # time.sleep(5)

    answer_text = WebDriverWait(browser, 15).until(
			EC.visibility_of_element_located(
				(By.CLASS_NAME, "smart-hints__hint"))
		)
    if answer_text.text != "Correct!":
        new_text = answer_text.text
        collected_results.append(new_text)
