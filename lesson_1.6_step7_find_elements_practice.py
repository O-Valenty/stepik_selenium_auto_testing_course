from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/huge_form.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for el in elements:
        el.send_keys('Something')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
    