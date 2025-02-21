
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    text_calc = browser.find_element(By.ID, "input_value")
    y = calc(text_calc.text)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(f"{y}")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    print(browser.switch_to.alert.text.split()[-1])


finally:
    time.sleep(5)
    browser.quit()