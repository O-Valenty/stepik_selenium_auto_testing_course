import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/find_link_text'
secret_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    target_link = browser.find_element(By.LINK_TEXT, secret_link)
    target_link.click()
    input1 = browser.find_element(By.NAME, 'first_name')
    input1.send_keys('Anna')
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Smirnova')
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Moskow')
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('USA')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()


