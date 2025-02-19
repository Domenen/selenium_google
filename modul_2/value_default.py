from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    people_radio = browser.find_element(By.ID, "peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    
    # 1
    # assert people_checked is not None, "People radio is not selected by default"

    # 2
    # assert people_checked == "true", "People radio is not selected by default"

    # 3
    # time.sleep(11)
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")

    # 4
    time.sleep(11)
    button_sub = browser.find_element(By.CLASS_NAME, "btn-default")
    disabled_button = button_sub.get_attribute("disabled")
    assert disabled_button == "true"

finally:
    time.sleep(5)
    browser.quit()