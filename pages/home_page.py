from selenium.webdriver.common.by import By
from base_page import BasePage
from cfg_sites import ConfigSite

class HomePage(BasePage):
    SEARCH_BOX =  (By.LINK_TEXT, 'Form Authentication')
    SEARCH_BUTTON = (By.LINK_TEXT, 'Login')
    SIGN_IN_BUTTON = (By.LINK_TEXT, "Inputs")
    CONTACT_US_BUTTON = (By.ID, "contact-link")

    # Використовуємо дані з конфігураційного класу
    HEADER_LINKS = ConfigSite.HEADER_LINKS
    SUPPORT_CENTER_LINK = (By.LINK_TEXT, 'About')
    SUPPORT_LINKS = ConfigSite.SUPPORT_LINKS

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_item(self, item):
        self.click_element(self.SEARCH_BOX)
        self.click_element(self.SEARCH_BUTTON)

    def go_to_sign_in(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def test_header_links(self):
        for locator in self.HEADER_LINKS:
            element = self.find_element(locator)
            if element:
                print(f"Посилання '{locator[1]}' знайдено")
                element.click()
                assert self.driver.current_url != self.base_url, f"Посилання '{locator[1]}' не призвело до переходу"
                self.open()
            else:
                print(f"Посилання '{locator[1]}' не знайдено")

    def go_to_support_center(self):
        self.click_element(self.SUPPORT_CENTER_LINK)

    def check_support_links(self):
        # Збереження поточного URL для повернення
        current_url = self.driver.current_url

        self.go_to_support_center()

        for locator in self.SUPPORT_LINKS:
            link = self.find_element(locator)
            assert link is not None, f"Посилання з текстом '{locator[1]}' не знайдено"
            link.click()

            assert self.driver.current_url != current_url, f"Посилання з текстом '{locator[1]}' не призвело до переходу"

            self.driver.get(current_url)
            self.go_to_support_center()

    def check_responsiveness(self):
        self.open()

        self.go_to_support_center()

        sizes = [(1920, 1080), (1366, 768), (1024, 768), (768, 1024), (360, 640)]
        for width, height in sizes:
            self.driver.set_window_size(width, height)
            self.driver.refresh()

            if ConfigSite.SIZE_TEST_PHRASE_1 in self.driver.page_source:
                print(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_1}' знайдений на розмірі екрану {width}x{height}")
            else:
                raise AssertionError(
                    f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_1}' не знайдений на розмірі екрану {width}x{height}")

            if ConfigSite.SIZE_TEST_PHRASE_2 in self.driver.page_source:
                print(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_2}' знайдений на розмірі екрану {width}x{height}")
            else:
                raise AssertionError(f"Елемент '{ConfigSite.SIZE_TEST_PHRASE_2}' не знайдений на розмірі екрану {width}x{height}")
