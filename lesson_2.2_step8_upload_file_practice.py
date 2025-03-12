from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'test.txt'
file_path = os.path.join(current_dir, file_name)

try:
    link = 'https://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Vasilisa')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Putilishna')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('login@example.com')
    upload_file = browser.find_element(By.NAME, 'file')
    upload_file.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()
finally:
    time.sleep(5)
    browser.quit()
