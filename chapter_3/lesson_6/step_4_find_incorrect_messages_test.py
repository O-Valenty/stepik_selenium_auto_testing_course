import math
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import stepik_credentials # учетные данные (объект с ключами login и password)

@pytest.fixture(scope="session")
def auth_browser():
    print("\n>>>>>> Запуск браузера для тестирования.")
    auth_browser = webdriver.Chrome()
    auth_browser.implicitly_wait(15) # задаем неявное ожидание для всех действий внутри браузера
    auth_browser.get("https://stepik.org/")
    # ждем появления навбара с кнопкой входа на сайт и нажимаем на нее
    singin_button = auth_browser.find_element(By.CLASS_NAME, "navbar__auth_login")
    singin_button.click()
    login_input = auth_browser.find_element(By.ID, "id_login_email")
    login_input.send_keys(stepik_credentials["login"])
    password_input = auth_browser.find_element(By.ID, "id_login_password")
    password_input.send_keys(stepik_credentials["password"])
    submit_singin_button = auth_browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    submit_singin_button.click()
    # ждем закрытия модалки ввода учетных данных
    WebDriverWait(auth_browser, 10).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "modal-dialog__content")))
    yield auth_browser
    print("\n>>>>>> Завершение работы браузера для тестов.")
    auth_browser.quit()
    
# Ссылки для теста
links = [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"
]

@pytest.mark.parametrize("link", links)
def test_the_shoul_has_correct_text(auth_browser, link):
    auth_browser.get(link)
    # проверяем, есть ли на странице кнопка "Решить снова" или "Начать сначала(сброс)" и нажимаем ее
    try:
        reset_answer_button = auth_browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        reset_answer_button.click()
        # подтверждаем действие в модальном окне, если требуется
        try:
            confirm = auth_browser.find_element(By.CLASS_NAME, "modal-popup__container")
            confirm_button = confirm.find_element(By.CSS_SELECTOR, "button:first-child")
            confirm_button.click()
            print("\n>>>>>> Нажата кнопка 'Начать сначала (сброс)' и дано подтверждение в модальном окне.")
        except NoSuchElementException:
            print("\n>>>>>> Нажата кнопка 'Решить снова'.")
    except NoSuchElementException:
        print("\n>>>>>> Кнопки 'Решить снова' или 'Начать сначала(сброс)' не найдены.")
        
    # ждем готовности поля ввода (может понадобиться, если сбрасывали решение)
    answer_input = WebDriverWait(auth_browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea")))
    # генерируем ответ непосредственно перед вводом в инпут
    answer = math.log(int(time.time()))
    answer_input.send_keys(str(answer))
    # ждем, пока кнопка "Отправить" станет кликабельна
    submit_answer_button = WebDriverWait(auth_browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    submit_answer_button.click()
    # получам результат проверки
    result = auth_browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    result_text = result.text
    assert result_text == "Correct!", f">>>>>> По ссылке {link} получено послание от НЛО: '{result_text}'."  
