# find_element(By.ID, value) — поиск по уникальному атрибуту id элемента.
# Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будете использовать
# этот метод, так как он наиболее стабильный;
# find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS.
# Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам.
# Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего
# вы будете использовать именно этот метод в ваших тестах;
# find_element(By.XPATH, value) — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element(By.NAME, value) — поиск по атрибуту name элемента;
# find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента;
# find_element(By.CLASS_NAME, value) — поиск по значению атрибута class;
# find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
# find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.


#find_element() - возвращает только ПЕРВЫЙ найденный элемент на странице
#find_elements() - используется, если нужно найти второй или последующие элементы на странице


# Каждый раз при открытии браузера browser = webdriver.Chrome() в системе создается процесс, который останется висеть,
# если вы вручную закроете окно браузера.
# Чтобы не остаться без оперативной памяти после запуска нескольких скриптов, всегда добавляйте к своим скриптам команду закрытия
# закрываем браузер после всех манипуляций
# browser.close() закрывает текущее окно браузера.
# Это значит, что если ваш скрипт вызвал всплывающее окно, или открыл что-то в новом окне или вкладке браузера,
# то закроется только текущее окно, а все остальные останутся висеть.
# browser.quit() закрывает все окна, вкладки, и процессы вебдрайвера, запущенные во время тестовой сессии

# Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках,
# проще всего использовать конструкцию try/finally

# Вариант без try/finally
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/simple_form_find_task.html')
button = browser.find_element(By.ID, 'submit_button')
button.click()
browser.quit()

# Вариант с try/finally

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    # даже если в коде внутри блока try произойдет какая-то ошибка, то код внутри блока finally выполнится в любом случае
    browser.quit()


