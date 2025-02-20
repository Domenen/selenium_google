from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    num_1 = int(browser.find_element(By.ID, "num1").text)
    num_2 = int(browser.find_element(By.ID, "num2").text)
    sum_num = num_1 + num_2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f"{sum_num}")

    button_submit = browser.find_element(By.CLASS_NAME, "btn-default")
    button_submit.click()



finally:
    time.sleep(10)
    browser.quit()