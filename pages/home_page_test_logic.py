import pytest
from home_page import HomePage
from selenium.webdriver.common.by import By

def test_search_item(driver):
    home_page = HomePage(driver)
    home_page.open()
    print("Тест пошуку елементів розпочався")
    home_page.search_for_item("dress")
    print("Тест пошуку елементів закінчився")


def test_navigate_to_sign_in(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_sign_in()


def test_header_links(driver):
    home_page = HomePage(driver)
    home_page.open()  # Открыть главную страницу
    print("Тест перевірки посилань у меню навігації сайту розпочався")
    home_page.test_header_links()
    print("Тест перевірки посилань у меню навігації сайту закінчився")

def test_support_center_links(driver):
    home_page = HomePage(driver)
    home_page.open()  # Открыть главную страницу

    print("Тест перевірки посилань у розділі Support Center розпочався")
    home_page.check_support_links()
    print("Тест перевірки посилань у розділі Support Center закінчився")
    # Додаткові перевірки можуть бути тут

def test_responsiveness(driver):
    home_page = HomePage(driver)
    home_page.check_responsiveness()  # Проверить адаптивность сайта