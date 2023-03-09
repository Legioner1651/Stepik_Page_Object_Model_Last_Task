import pytest
import time
from .pages.product_page import ProductPage
from .pages.base_page import Product
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_can_add_product_to_basket(browser, link):
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу с товаром.
    page.open()
    # 3. Получаем название книги.
    name = page.get_name_product_catalogue()
    # 4. Получаем цену книги.
    price = page.get_price_product_catalogue()
    # 5. Инициализируем объект товар = книга
    book = Product(name, price)
    # 6. Добавляем товар в корзину.
    page.add_to_basket()
    # 7. Проверка сообщения об успешности добавления товара в корзину
    page.should_be_success_message()
    # 8. Проверка сообщения, что корзина соответствует условиям активного предложения
    page.should_be_message_success_accordance()
    # 9. Проверка, что в сообщении название товара не поменялось
    page.should_be_name_added_product(book)
    # 10. Проверка, что стоимость корзины совпадает с ценой товара.
    page.should_be_equal_price_added_product(book)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Добавляем товар в корзину
    page.add_to_basket()
    # 4. Проверяем, что после добавления нет сообщения об успехе
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Проверяем, что без добавления нет сообщения об успехе
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Добавляем товар в корзину
    page.add_to_basket()
    # 4. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_disappeared_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Проверяем существовании кнопки входа/регистрации
    page.should_be_login_link()
    

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Проверяем существовании кнопки входа/регистрации
    page.should_be_login_link()
    # 4. Переходим на страницу вход/регистрация
    page.go_to_login_page()
    # 5. Проверяем наличие полей на странице вход/регистрация
    page_login = LoginPage(browser, browser.current_url)
    # 6. Проверка существования страницы вход/регистрация
    page_login.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Гость открывает страницу товара
    page.open()
    # 3. Переходит в корзину по кнопке в шапке
    page.should_be_basket_link()
    page.go_to_basket_page()
    # 4. Ожидаем, что в корзине нет товаров
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty()
    # 5. Ожидаем, что есть текст о том что корзина пуста
    page_basket.should_be_text_that_basket_is_empty()

    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
        self.page_login = LoginPage(browser, self.link)
        # 2. Открываем страницу регистрации:
        self.page_login.open()
        # 3. зарегистрировать нового пользователя:
        self.email = str(time.time()) + "@ngs.ru"
        self.password = "qweqwe1234"
        self.page_login.register_new_user(self.email, self.password)
        # 4. Проверяем, что пользователь залогинен:
        self.page_login.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
        page = ProductPage(browser, link)
        # 2. Открываем страницу товара
        page.open()
        # 3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page.should_not_be_success_message()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
        page = ProductPage(browser, link)
        # 2. Открываем страницу с товаром.
        page.open()
        # 3. Получаем название книги.
        name = page.get_name_product_catalogue()
        # 4. Получаем цену книги.
        price = page.get_price_product_catalogue()
        # 5. Инициализируем объект товар - книга
        book = Product(name, price)
        # 6. Добавляем товар в корзину.
        page.add_to_basket()
        # 7. Проверка сообщения об успешности добавления товара в корзину
        page.should_be_success_message()
        # 8. Проверка сообщения, что корзина соответствует условиям активного предложения
        page.should_be_message_success_accordance()
        # 9. Проверка в сообщении, что название товара не поменялось
        page.should_be_name_added_product(book)
        # 10. Проверка, что стоимость корзины совпадает с ценой товара.
        page.should_be_equal_price_added_product(book)
