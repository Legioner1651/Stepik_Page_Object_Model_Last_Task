import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
#from selenium.webdriver.common.by import By

# pytest -s -v test_main_page.py > log.log
# pytest -v --tb=line --language=en test_main_page.py > log.log
# pytest -v --tb=line --language=en -m need_review test_main_page.py > log.log

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # (v.4.3 step 2)
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#link = "http://selenium1py.pythonanywhere.com/"

# pytest -v -m login_guest --tb=line --language=en test_main_page.py > log.log
@pytest.mark.login_guest
class TestLoginFromMainPage():

    # pytest -s -v test_main_page.py::TestLoginFromMainPage::test_guest_can_go_to_login_page > log.log
    def test_guest_can_go_to_login_page(self, browser):      # (v.4.1 step 6)(v.4.2 step 4)?
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу  (v.4.2 step 4)
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина (v.4.2 step 4), (v.4.2 step 9)
        login_page = LoginPage(browser, browser.current_url)  # (v.4.2 step 9)
        login_page.should_be_login_page()                     # (v.4.2 step 9)

    # pytest -s -v test_main_page.py::TestLoginFromMainPage::test_guest_should_see_login_link > log.log
    def test_guest_should_see_login_link(self, browser):  # (v.4.2 step 5) будет проверять наличие ссылки
        page = MainPage(browser, link)              # (v.4.2 step 5)
        page.open()                                 # (v.4.2 step 5)
        page.should_be_login_link()                 # (v.4.2 step 5) - Проверка, что есть ссылка, которая ведет на логин
    

# pytest -s -v test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page > log.log
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):   # (v.4.3 step 10)
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    # 1. Гость открывает главную страницу                                        # (v.4.3 step 10)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке сайта
    page.should_be_basket_link()
    page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty()
    # 4. Ожидаем, что есть текст о том что корзина пуста
    page_basket.should_be_text_that_basket_is_empty()
