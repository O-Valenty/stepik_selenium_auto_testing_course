from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))

try:
    link = 'https://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    result = function_calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
finally:
    time.sleep(5)
    browser.quit()
    