from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))

try:
    link = 'https://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    first_tab = browser.window_handles[0]
    fly_button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    fly_button.click()
    second_tab = browser.window_handles[1]
    browser.switch_to.window(second_tab)

    x = browser.find_element(By.ID, 'input_value').text
    result = function_calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
finally:
    time.sleep(6)
    browser.quit()
