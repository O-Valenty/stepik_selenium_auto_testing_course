from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))

try:
    link = 'https://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element(By.ID, 'input_value').text
    function_result = function_calc(x_value)
    input = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(function_result)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()