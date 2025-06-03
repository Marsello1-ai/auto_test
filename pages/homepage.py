# ОПИСАНИЕ ДОМАШНЕЙ СТРАНЦЫ, ДЛЯ КЛИКОВ И ПРОЧЕГО
from selenium.webdriver.common.by import By


class HomePage:


    def __init__(self, browser):
        self.browser = browser



    def open(self):
        self.browser.get('https://www.demoblaze.com/index.html')  # открывает страницу


    def click_galaxy_s6(self):
        galaxy_s6 = self.browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]') # ищет элемент на странице, ищет по ссылке на тексте
        galaxy_s6.click()  # кликает по нему


    def click_monitor(self, ):
        monitor_link = self.browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')  # ищет элемент на странице, ищет по ссылке на тексте
        monitor_link.click()  # кликает по нему



    def check_products_counts(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, value='.card')  # ищет элемент на следующей стр, с префиксом s несколько элементов
        assert len(monitors) == count  # тест заканчивается проеверяем