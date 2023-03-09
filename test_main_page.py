import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        # 2. Переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        # 2. Проверка, что существует ссылка на логин
        page.should_be_login_link()
    

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес главной страницы
    page = MainPage(browser, link)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке сайта
    page.should_be_basket_link()
    page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty()
    # 4. Ожидаем, что есть текст о том что корзина пуста
    page_basket.should_be_text_that_basket_is_empty()
