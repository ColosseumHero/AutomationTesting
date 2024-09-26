import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Ініціалізуємо браузер Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # Закриваємо браузер після тесту
    driver.quit()


