import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Створюємо об'єкт для налаштувань Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Безголовий режим
    chrome_options.add_argument("--no-sandbox")  # Потрібно для серверів CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Оптимізація для обмежених ресурсів

    # Ініціалізуємо браузер Chrome з опціями
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    # Закриваємо браузер після тесту
    driver.quit()


