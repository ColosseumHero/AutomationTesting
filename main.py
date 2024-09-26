import pytest
import sys
import os

# Добавьте путь к папке с тестами
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

if __name__ == "__main__":
    # Запуск тестов из файла home_page_test_logic.py
    pytest.main(["-q", "--tb=line", "pages/home_page_test_logic.py"])