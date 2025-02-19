from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    chest = browser.find_element(By.ID, "treasure")
    valuex_chest = chest.get_attribute("valuex")

    y = calc(valuex_chest)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(f"{y}")

    check_box = browser.find_element(By.ID, "robotCheckbox")
    check_box.click()

    radiola = browser.find_element(By.ID, "robotsRule")
    radiola.click()

    button_smb = browser.find_element(By.CLASS_NAME, "btn-default")
    button_smb.click()    

finally:
    time.sleep(10)
    browser.quit()