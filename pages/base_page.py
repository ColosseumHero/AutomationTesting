from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from cfg_sites import ConfigSite

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ConfigSite.BASE_URL

    def open(self, url=None):
        """Відкривання сторінки"""
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.base_url)

    def find_element(self, locator, timeout=ConfigSite.TIMEOUT_FACTOR_MIN):
        """Знаходження елемента на сторінці"""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            print(f"Елемент {locator} знайдено")
            return element
        except TimeoutException:
            print(f"Елемент {locator} не знайдено протягом {timeout} секунд")
            return None

    def find_elements(self, locator, timeout=ConfigSite.TIMEOUT_FACTOR_MIN):
        """Знаходження кілька елементів на сторінці"""
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            print(f"Елементи {locator} знайдено")
            return elements
        except TimeoutException:
            print(f"Елементи {locator} не знайдено протягом {timeout} секунд")
            return []

    def click_element(self, locator, timeout=ConfigSite.TIMEOUT_FACTOR_MAX):
        """Натискання на елемент"""
        element = self.find_element(locator, timeout)
        if element:
            element.click()

    def input_text(self, locator, text, timeout=ConfigSite.TIMEOUT_FACTOR_MAX):
        """Введення тексту у поле"""
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
