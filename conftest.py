import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless') # отключаем юай для прохождения тестов
    browser = webdriver.Chrome(options = options) # открывает бразуер и использует опции при запуске
    browser.maximize_window() # делает его на весь экран
    browser.implicitly_wait(3) # ожидание 3 секунды, перед падением, только после истечения упадет тест
    yield browser # пост условия
    browser.close() #закрывает браузер после тестов, можно прописать, если не закрывается