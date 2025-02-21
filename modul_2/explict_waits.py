from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = browser.find_element(By.ID, "book")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), ("$100"))
        )
    button.click()

    x = browser.find_element(By.ID, "input_value")
    y = calc(x.text)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(f"{y}")

    button_smb = browser.find_element(By.ID, "solve")
    button_smb.click()



finally:
    time.sleep(5)
    browser.quit()