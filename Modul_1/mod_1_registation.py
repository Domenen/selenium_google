
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def testing_url(link):
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, "first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "first_block input.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CLASS_NAME, "first_block input.third")
        input3.send_keys("Email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    except Exception as e:
        print(f"ошибка ----{e}") #Вывод ошибки

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

testing_url("http://suninjuly.github.io/registration1.html")
testing_url("http://suninjuly.github.io/registration2.html")