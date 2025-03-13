from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def math_calc(a, b):
    return str(int(a) + int(b))

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID, 'num1').text
    b = browser.find_element(By.ID, 'num2').text
    dropdown = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown.select_by_value(math_calc(a, b))
    button = browser.find_element(By.CSS_SELECTOR, 'button,btn')
    button.click()

finally:
    time.sleep(7)
    browser.quit()