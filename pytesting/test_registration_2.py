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


links = ["https://stepik.org/lesson/236895/step/1"]
        #  "https://stepik.org/lesson/236896/step/1", 
        #  "https://stepik.org/lesson/236897/step/1", 
        #  "https://stepik.org/lesson/236898/step/1", 
        #  "https://stepik.org/lesson/236899/step/1",
        #  "https://stepik.org/lesson/236903/step/1", 
        #  "https://stepik.org/lesson/236904/step/1",
        #  "https://stepik.org/lesson/236905/step/1"]


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

    button_auth = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(By.CLASS_NAME, "navbar__auth"))
    button_auth.click()

    input_name = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(By.CSS_SELECTOR, "input[name='login']"))
    input_name.send_keys(f"{LOGIN}")

    input_pass = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    input_pass.send_keys(f"{PASSWORD}")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    input_textarea = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(By.CLASS_NAME,
                                              "string-quiz__textarea"))
    answer = math.log(int(time.time()))
    input_textarea.send_keys(f"{answer}")

    button_send = browser.find_element(By.CLASS_NAME, "submit-submission")
    button_send.click()

    answer_text = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(By.CLASS_NAME, "attempt-message")
    )
    print(answer_text.text == "Correct!")
