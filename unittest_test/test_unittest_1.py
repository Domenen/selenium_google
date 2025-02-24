from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
import time


class TestLink(unittest.TestCase):
    def test_link1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CLASS_NAME, "first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "first_block input.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CLASS_NAME, "first_block input.third")
        input3.send_keys("Email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        msg_normal = "Congratulations! You have successfully registered!"
        self.assertEqual(
            msg_normal, welcome_text, "fail in 1 link"
        )
        
    def test_link2(self):
        # Тест специально провален, чтобы наглядно видеть как это выглядит
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CLASS_NAME, "first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "first_block input.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CLASS_NAME, "first_block input.third")
        input3.send_keys("Email")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        msg_normal = "Congratulations! You have successfully registered!"
        self.assertEqual(
            msg_normal, welcome_text, "fail in 2 link"
        )
        


if __name__ == "__main__":
    unittest.main()