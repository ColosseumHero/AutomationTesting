from selenium.webdriver.common.by import By

class ConfigSite:
    # URL головної сторінки
    BASE_URL = "https://www.python.org/doc/"
    #BASE_URL = "http://automationpractice.com/"
    #BASE_URL = "https: // www.inmotionhosting.com /"
    #BASE_URL = "https://en.wikipedia.org/wiki/Transfer"

    # Тестові фрази
    HEADER_LINKS = [
        (By.LINK_TEXT, "About"),
        (By.LINK_TEXT, 'Downloads'),
        (By.LINK_TEXT, 'Documentation'),
        (By.LINK_TEXT, 'Community'),
        (By.LINK_TEXT, 'Success Stories'),
        (By.LINK_TEXT, 'News'),
        (By.LINK_TEXT, 'Events'),
    ]

    SUPPORT_LINKS = [
        (By.LINK_TEXT, "Beginner's Guide, Programmers"),
        (By.LINK_TEXT, "Beginner's Guide, Non-Programmers"),
        (By.LINK_TEXT, "Beginner's Guide, Download & Installation"),
        (By.LINK_TEXT, "Code sample and snippets for Beginners"),
    ]

    #SIZE_TEST_PHRASE_1 = "German science-fiction"
    #SIZE_TEST_PHRASE_2 = "an international expedited bank-to-bank funds transfer"
    #SIZE_TEST_PHRASE_1 = "Website Guide for New Customers"
    #SIZE_TEST_PHRASE_2 = "Website Transfers"
    SIZE_TEST_PHRASE_1 = "Python's documentation, tutorials, and guides are constantly evolving"
    SIZE_TEST_PHRASE_2 = "Get started here, or scroll down for documentation"

    # Тайм-аути
    TIMEOUT_FACTOR_MAX = 10
    TIMEOUT_FACTOR_MIN = 3