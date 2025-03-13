import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_registration_success(self):
        try:
            link = 'http://suninjuly.github.io/registration1.html'
            browser = webdriver.Chrome()
            browser.get(link)

            first_name_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first') # "input.first[required]" / "input.first:required"
            first_name_input.send_keys('Artur')
            last_name_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second') # "input.second[required]" / "input.second:required"
            last_name_input.send_keys('King')
            email_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third') # "input.third[required]" / "input.third:required"
            email_input.send_keys('example@mail.com')
            button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
            welcome_text = welcome_text_elt.text  # записываем в переменную welcome_text текст из элемента welcome_text_elt

            self.assertEqual ('Congratulations! You have successfully registered!', welcome_text, "Expexted successful registration text, but didn't get it.")

        finally:
            time.sleep(5)
            browser.quit()

    def test_registration_denied(self):
        try:
            link = 'http://suninjuly.github.io/registration2.html'
            browser = webdriver.Chrome()
            browser.get(link)

            first_name_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first') # "input.first[required]" / "input.first:required"
            first_name_input.send_keys('Artur')
            last_name_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second') # "input.second[required]" / "input.second:required"
            last_name_input.send_keys('King')
            email_input = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third') # "input.third[required]" / "input.third:required"
            email_input.send_keys('example@mail.com')
            button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
            welcome_text = welcome_text_elt.text  # записываем в переменную welcome_text текст из элемента welcome_text_elt

            self.assertEqual ('Congratulations! You have successfully registered!', welcome_text, "Expexted successful registration text, but didn't get it.")

        finally:
            time.sleep(5)
            browser.quit()

if __name__ == "__main__":
    unittest.main()