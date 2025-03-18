import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_guest_should_see_login_link(auth_browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    auth_browser.get(link)
    auth_browser.find_element(By.CSS_SELECTOR, "#login_link")

@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, auth_browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        auth_browser.get(link)
        auth_browser.find_element(By.CSS_SELECTOR, "#login_link")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, auth_browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        auth_browser.get(link)
        auth_browser.find_element(By.CSS_SELECTOR, ".navbar.primary")
        # этот тест тоже запустится дважды