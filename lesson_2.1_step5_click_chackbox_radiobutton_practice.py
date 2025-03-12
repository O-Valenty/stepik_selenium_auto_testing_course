from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))


try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    function_result = function_calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(function_result)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()