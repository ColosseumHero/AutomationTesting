import pytest
import time

def test_example():
    # Простий тест для перевірки, що 1 + 1 дорівнює 2
    time.sleep(59)
    assert 1 + 1 == 2

def test_string():
    # Перевірка, що рядки рівні
    assert "Hello" == "Hello"

def test_in_list():
    # Перевірка, що число є в списку
    num_list = [1, 2, 3, 4, 5]
    assert 3 in num_list

def test_in_list_new():
    # Перевірка, що число є в списку
    num_list = [1, 2, 3, 4, 5]
    assert 3 in num_list

def test_in_list_another():
    # Перевірка, що число є в списку
    num_list = [1, 2, 3, 4, 5]
    assert 3 in num_list

