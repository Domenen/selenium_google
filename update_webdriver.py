import os
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = shutil.which("chromedriver")
service = Service(chrome_driver_path)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


driver.get(" https://www.google.com ")
print("ChromeDriver обновлен и работает!")
driver.quit()