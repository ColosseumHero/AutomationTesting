from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless режим
    chrome_options.add_argument("--no-sandbox")  # Для работы в окружениях CI/CD
    chrome_options.add_argument("--disable-dev-shm-usage")  # Для минимизации использования shared memory
    chrome_options.add_argument("--disable-gpu")  # Отключаем GPU, часто помогает при headless тестировании
    chrome_options.add_argument("--remote-debugging-port=9222")  # Указываем порт для отладки

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


