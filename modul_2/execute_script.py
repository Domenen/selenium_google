
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    text_calc = browser.find_element(By.ID, "input_value")
    x = text_calc.text
    y = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(f"{y}")

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radiola = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiola)
    time.sleep(1)
    radiola.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(1)

# except Exception as e:
#     print(f"ошибка ----{e}") #Вывод ошибки

finally:
    time.sleep(5)
    browser.quit()
