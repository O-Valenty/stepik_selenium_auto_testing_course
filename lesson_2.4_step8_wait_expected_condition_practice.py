from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from math import log, sin
import time

def function_calc(x):
    return str(log(abs(12 * sin((int(x))))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    price = browser.find_element(By.ID, 'price')
    target_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    x = browser.find_element(By.ID, 'input_value').text
    result = function_calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)
    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
    
