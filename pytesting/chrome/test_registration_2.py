import os
import time
import math
import pytest
import logging

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LOGIN = os.getenv("LOGIN") or "login"
PASSWORD = os.getenv("PASSWORD") or "password"

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="session")
def collected_results():
    results = []
    message_text = ""
    yield results
    print("\nРезультат всех тестов:")
    for result in results:
        message_text +=result
    print(message_text)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")  # Игнорировать SSL-ошибки
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--enable-unsafe-swiftshader")
    chrome_options.add_argument("--disable-extensions")  # Отключить расширения
    chrome_options.add_argument("--disable-notifications")  # Отключить уведомления
    chrome_options.add_argument("--disable-gpu")  # Отключить GPU (может ускорить запуск)
    chrome_options.add_argument("--no-sandbox")  # Отключить песочницу
    chrome_options.add_argument("--disable-dev-shm-usage")  # Уменьшить использование памяти
    chrome_options.add_argument("--headless")   # Разрешить небезопасные локальные соединения
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('site_link', links)
def test_guest_should_see_login_link(browser,
                                     site_link,
                                     collected_results):
    link = f"{site_link}"
    browser.get(link)

    button_auth = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "navbar__auth")
    ))
    button_auth.click()

    input_name = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[name='login']")
    ))
    input_name.send_keys(LOGIN)

    input_pass = browser.find_element(
        By.CSS_SELECTOR, "input[name='password']"
    )
    input_pass.send_keys(PASSWORD)

    button = browser.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    button.click()

    time.sleep(5)
    textarea_free = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "quiz-component"))
    ).get_attribute("data-state")
    
    if textarea_free != "correct":
        input_textarea = browser.find_element(
            By.CLASS_NAME, "string-quiz__textarea"
        )
        answer = str(math.log(int(time.time())))
        input_textarea.send_keys(answer)

        current_value = input_textarea.get_attribute("value")
        if not current_value:
            logger.warning(
                "Текст не был вставлен, создаем новый ответ и вставляем его.")
            new_answer = str(math.log(int(time.time())))
            max_attempts = 3
            for attempt in range(max_attempts):
                input_textarea.clear()
                input_textarea.send_keys(new_answer)
                current_value = input_textarea.get_attribute("value")
                if current_value:
                    break
                logger.warning(
                    f"Попытка {attempt + 1}: текст не был вставлен.")

        if current_value:
            try:
                button_smb = WebDriverWait(browser, 15).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button.submit-submission")
                ))
                button_smb.click()
            except StaleElementReferenceException:
                button_smb = WebDriverWait(browser, 15).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button.submit-submission")
                ))
                button_smb.click()
        else:
            logger.error("Ошибка: текст не был вставлен в поле.")

    answer_text = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "smart-hints__hint")
    ))
    if answer_text.text != "Correct!":
        collected_results.append(answer_text.text)