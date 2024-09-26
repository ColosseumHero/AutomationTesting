import time
from selenium.webdriver.common.by import By
from base_page import BasePage
from cfg_sites import ConfigSite

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")
    SIGN_IN_BUTTON = (By.CLASS_NAME, "login")
    CONTACT_US_BUTTON = (By.ID, "contact-link")

    HEADER_LINKS = [
        (By.LINK_TEXT, 'Web Hosting'),
        (By.LINK_TEXT, 'WordPress'),
        (By.LINK_TEXT, 'VPS Hosting'),
        (By.LINK_TEXT, 'Dedicated Servers'),
        (By.LINK_TEXT, 'Domains'),
        (By.LINK_TEXT, 'Why Us')
    ]

    # Определение локаторов для раздела Support Center
    SUPPORT_CENTER_LINK = (By.LINK_TEXT, 'Support Center')

    # Определение локаторов для ссылок на странице Support Center
    SUPPORT_LINKS = [
        (By.LINK_TEXT, 'Website Guide for New Customers'),
        (By.LINK_TEXT, 'Website Transfers'),
        (By.LINK_TEXT, 'cPanel Login'),
        (By.LINK_TEXT, 'FTP Connection Settings'),
        (By.LINK_TEXT, 'Where to Upload Files')
    ]

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_item(self, item):
        self.input_text(self.SEARCH_BOX, item)
        self.click_element(self.SEARCH_BUTTON)

    def go_to_sign_in(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def test_header_links(self):
        """Тестирует все ссылки в шапке сайта"""
        for locator in self.HEADER_LINKS:
            element = self.find_element(locator)
            if element:
                print(f"Ссылка с текстом '{locator[1]}' найдена")
                element.click()
                assert self.driver.current_url != self.base_url, f"Ссылка с текстом '{locator[1]}' не привела к переходу"
                self.open()  # Вернуться на главную страницу для следующего теста
            else:
                print(f"Ссылка с текстом '{locator[1]}' не найдена")

    def go_to_support_center(self):
        """Переход в раздел Support Center"""
        self.click_element(self.SUPPORT_CENTER_LINK)

    def check_support_links(self):
        """Проверка кликабельности и правильности ссылок на странице Support Center"""
        # Сохранить текущий URL для возврата
        current_url = self.driver.current_url

        self.go_to_support_center()

        for locator in self.SUPPORT_LINKS:
            link = self.find_element(locator)
            assert link is not None, f"Ссылка с текстом '{locator[1]}' не найдена"
            link.click()

            # Убедиться, что мы на странице по новой ссылке
            assert self.driver.current_url != current_url, f"Ссылка '{locator[1]}' не привела к переходу"

            # Вернуться на страницу Support Center
            self.driver.get(current_url)
            self.go_to_support_center()  # Навигация обратно к Support Center после загрузки страницы

    def check_responsiveness(self):
        """Проверяет адаптивность сайта на различных размерах экрана"""
        # Сначала переходим на главную страницу
        self.open()

        # Переходим на страницу Support Center
        self.go_to_support_center()

        sizes = [(1920, 1080), (1366, 768), (1024, 768), (768, 1024), (360, 640)]
        for width, height in sizes:
            self.driver.set_window_size(width, height)
            self.driver.refresh()  # Обновляем страницу, чтобы увидеть изменения

            # Добавляем проверку наличия элемента и вывод сообщения
            if ConfigSite.SIZE_TEST_PHRASE_1 in self.driver.page_source:
                print(f"Элемент '{ConfigSite.SIZE_TEST_PHRASE_1}' найден на размере экрана {width}x{height}")
            else:
                raise AssertionError(
                    f"Элемент '{ConfigSite.SIZE_TEST_PHRASE_1}' не найден на размере экрана {width}x{height}")

            # Можно добавить больше проверок или вывода информации о проверке, если нужно
            # Например:
            if ConfigSite.SIZE_TEST_PHRASE_2 in self.driver.page_source:
                print(f"Элемент '{ConfigSite.SIZE_TEST_PHRASE_2}' найден на размере экрана {width}x{height}")
            else:
                raise AssertionError(f"Элемент '{ConfigSite.SIZE_TEST_PHRASE_2}' не найден на размере экрана {width}x{height}")

            # Аналогично для других элементов, если нужно добавить больше проверок