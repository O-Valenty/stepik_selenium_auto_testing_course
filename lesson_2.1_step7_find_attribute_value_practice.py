from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))

try:
    link = 'https://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)
    chest_img = browser.find_element(By.ID, 'treasure')
    x = chest_img.get_attribute('valuex')
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
    time.sleep(6)
    browser.quit()

   
