from selenium.webdriver.common.by import By

class ConfigSite:
    # URL головної сторінки
    BASE_URL = "https://the-internet.herokuapp.com/"
    #BASE_URL = "http://automationpractice.com/"
    #BASE_URL = "https: // www.inmotionhosting.com /"
    #BASE_URL = "https://en.wikipedia.org/wiki/Transfer"

    # Тестові фрази
    HEADER_LINKS = [
        (By.LINK_TEXT, "Broken Images"),
        (By.LINK_TEXT, 'Challenging DOM'),
        (By.LINK_TEXT, 'Checkboxes'),
        (By.LINK_TEXT, 'Context Menu'),
        (By.LINK_TEXT, 'Digest Authentication'),
    ]

    SUPPORT_LINKS = [
        (By.LINK_TEXT, 'About'),
        (By.LINK_TEXT, 'Contact Us'),
        (By.LINK_TEXT, 'Portfolio'),
        (By.LINK_TEXT, 'Gallery'),
    ]

    #SIZE_TEST_PHRASE_1 = "German science-fiction"
    #SIZE_TEST_PHRASE_2 = "an international expedited bank-to-bank funds transfer"
    #SIZE_TEST_PHRASE_1 = "Website Guide for New Customers"
    #SIZE_TEST_PHRASE_2 = "Website Transfers"
    SIZE_TEST_PHRASE_1 = "Available Examples"
    SIZE_TEST_PHRASE_2 = "Welcome to the-internet"

    # Тайм-аути
    TIMEOUT_FACTOR_MAX = 10
    TIMEOUT_FACTOR_MIN = 3