# ОПИСАНИЕ СТРАНИЦ НА КОТОРЫХ ПРОИСХОДИТ ТЕСТИРОВАНИЕ

from selenium.webdriver.common.by import By


class ProductPage:



    def __init__(self, browser):
        self.browser = browser


    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, value='h2')  # ищет элемент на следующей стр
        assert page_title.text == title  # тест заканчивается проеверяем, используем переменную которую передадим при вызове функции



