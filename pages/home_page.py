import time
from selenium.webdriver.common.by import By
from base_page import BasePage
from cfg_sites import ConfigSite

class HomePage(BasePage):
    SEARCH_BOX =  (By.LINK_TEXT, 'Log in')
    SEARCH_BUTTON = (By.LINK_TEXT, 'Create account')
    SIGN_IN_BUTTON = (By.CLASS_NAME, "vector-header-container")
    CONTACT_US_BUTTON = (By.ID, "contact-link")

    HEADER_LINKS = [
        (By.LINK_TEXT, 'Talk'),
        (By.LINK_TEXT, 'Edit'),
        (By.LINK_TEXT, 'View history'),
    ]

    # Определение локаторов для раздела Support Center
    SUPPORT_CENTER_LINK = (By.LINK_TEXT, 'Finance')

    # Определение локаторов для ссылок на странице Support Center
    SUPPORT_LINKS = [
        (By.LINK_TEXT, 'Transfer payment'),
        (By.LINK_TEXT, 'Balance transfer'),
        (By.LINK_TEXT, 'Money transfer (disambiguation)'),
        (By.LINK_TEXT, 'Wire transfer'),
    ]

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_item(self, item):
        self.click_element(self.SEARCH_BOX)
        self.click_element(self.SEARCH_BUTTON)

    def go_to_sign_in(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def test_header_links(self):
        """Тестирует все ссылки в шапке сайта"""
        for locator in self.HEADER_LINKS:
            element = self.find_element(locator)
            if element:
                print(f"Посилання '{locator[1]}' знайдено")
                element.click()
                assert self.driver.current_url != self.base_url, f"Посилання '{locator[1]}' не призвело до переходу"
                self.open()  # Вернуться на главную страницу для следующего теста
            else:
                print(f"Посилання '{locator[1]}' не знайдено")

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
            assert link is not None, f"Посилання з текстом '{locator[1]}' не знайдено"
            link.click()

            # Убедиться, что мы на странице по новой ссылке
            assert self.driver.current_url != current_url, f"Посилання з текстом '{locator[1]}' не призвело до переходу"

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
                print(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_1}' знайдений на розмірі екрану {width}x{height}")
            else:
                raise AssertionError(
                    f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_1}' не знайдений на розмірі екрану {width}x{height}")

            # Можно добавить больше проверок или вывода информации о проверке, если нужно
            # Например:
            if ConfigSite.SIZE_TEST_PHRASE_2 in self.driver.page_source:
                print(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_2}' знайдений на розмірі екрану {width}x{height}")
            else:
                raise AssertionError(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_2}' не знайдений на розмірі екрану {width}x{height}")

            # Аналогично для других элементов, если нужно добавить больше проверок