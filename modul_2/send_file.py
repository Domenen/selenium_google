
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 



try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input_1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input_1.send_keys("firstname")

    input_2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input_2.send_keys("lastname")

    input_3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input_3.send_keys("email")


    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'random_text.txt')           # добавляем к этому пути имя файла 
    send_file = browser.find_element(By.ID, "file")
    send_file.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    print(browser.switch_to.alert.text.split()[-1])
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
