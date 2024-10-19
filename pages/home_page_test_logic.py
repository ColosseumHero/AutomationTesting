from home_page import HomePage

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
    home_page.open()  # Відкриття головної сторінки сайту
    print("Тест перевірки посилань у меню навігації сайту розпочався")
    home_page.test_header_links()
    print("Тест перевірки посилань у меню навігації сайту закінчився")

def test_support_center_links(driver):
    home_page = HomePage(driver)
    home_page.open()  # Відкриття додаткової сторінки сайту

    print("Тест перевірки посилань у розділі About розпочався")
    home_page.check_support_links()
    print("Тест перевірки посилань у розділі About закінчився")
    # Додаткові перевірки

def test_responsiveness(driver):
    home_page = HomePage(driver)
    home_page.check_responsiveness()  # Перевірка адаптивності сайту

