import os
import time
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

LOGIN = os.getenv("LOGIN") or "login"
PASSWORD = os.getenv("PASSWORD") or "password"


link = "https://stepik.org/lesson/236895/step/1"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)

    button_auth = browser.find_element(By.CLASS_NAME, "navbar__auth")
    button_auth.click()
    time.sleep(3)

    input_name = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    input_name.send_keys(f"{LOGIN}")

    input_pass = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    input_pass.send_keys(f"{PASSWORD}")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()