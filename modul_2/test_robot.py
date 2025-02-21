
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    text_calc = browser.find_element(By.ID, "input_value")
    x = text_calc.text
    y = calc(x)
    print(y)

    input_1 = browser.find_element(By.CSS_SELECTOR, "div.form-group input#answer")
    input_1.send_keys(f"{y}")

    check_box = browser.find_element(By.CSS_SELECTOR, "div.form-check-custom input[type=checkbox]")
    check_box.click()

    radiola = browser.find_element(By.CSS_SELECTOR, "div.form-check input#robotsRule")
    radiola.click()

    button = browser.find_element(By.CSS_SELECTOR, "button[type=submit]")
    button.click()

    time.sleep(1)

except Exception as e:
    print(f"ошибка ----{e}") #Вывод ошибки

finally:
    time.sleep(5)
    browser.quit()
