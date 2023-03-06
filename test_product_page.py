import pytest
import time
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.base_page import Product
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# pytest -s -v test_product_page.py > log.log
# pytest -v --tb=line  test_product_page.py > log.log

email = str(time.time()) + "@fakemail.org"      # (v.4.3 step 13)

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#link = "http://selenium1py.pythonanywhere.com/"

# pytest -s -v test_product_page.py::test_guest_can_add_product_to_basket > log.log
# pytest -v --tb=line  test_product_page.py::test_guest_can_add_product_to_basket > log.log

#@pytest.mark.need_review                                # (v.4.3 step 14)  (v.3.5 step 2)     запуск      pytest -v --tb=line --language=en -m need_review test_product_page.py
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
#def test_guest_can_add_product_to_basket(browser):	# (v.4.3 step 2) # (v.4.3 step 14)
def test_guest_can_add_product_to_basket(browser, link):
    time_0 = time.time()
    #print('* link = ' + str(link))
    print('** Star test_guest_can_add_product_to_basket **, time = ' + str(time.time() - time_0))
    #link = "http://selenium1py.pythonanywhere.com/"
    # 2. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 3. Открываем страницу с товаром.
    print('** Start page.open() **, time = ' + str(time.time() - time_0))   # big lag
    page.open()                                                             # big lag   41
    print('** End page.open() **, time = ' + str(time.time() - time_0))
    # 4. Получаем название книги.
    name = page.get_name_product_catalogue()
    print('** End page.get_name_product() **, time = ' + str(time.time() - time_0))
    # 5. Получаем цену книги.
    price = page.get_price_product_catalogue()
    print('** End page.get_price_product() **, time = ' + str(time.time() - time_0))
    # 6. Инициалируем объект товар - книга
    book = Product(name, price)
    # 7. Добавляем товар в корзину.
    print('** Start page.add_to_basket() **, time = ' + str(time.time() - time_0))
    page.add_to_basket()          # нажимаем на кнопку добавить в корзину и выполняем метод страницы — переходим на страницу логина # big lag   55
    print('** Stop page.add_to_basket() **, time = ' + str(time.time() - time_0))
    #time.sleep(30)                                          # для тестирования
    # 8. Проверка сообщения об успешности добавления товара в корзину
    print('** Begin page.checking_of_confirmation_of_successful_addition() **, time = ' + str(time.time() - time_0))
    page.checking_of_confirmation_of_successful_addition()  # big lag 25
    print('** End page.checking_of_confirmation_of_successful_addition() **, time = ' + str(time.time() - time_0))
    # 9. Проверка собщения, что корзина соответствует условиям активного предложения
    page.checking_of_confirmation_of_deferred_benefit_offer()
    print('** End page.checking_of_confirmation_of_deferred_benefit_offer() **, time = ' + str(time.time() - time_0))
    # 10. Проверка в сообщении, что название товара не поменялось
    page.checking_that_product_name_has_not_changed(book)
    print('** End page.checking_that_product_name_has_not_changed() **, time = ' + str(time.time() - time_0))
    # 11. Проверка, что стоимость корзины совпадает с ценой товара.
    page.checking_that_price_has_not_changed(book)
    print('** End page.checking_that_price_has_not_changed() **, time = ' + str(time.time() - time_0))
    #time.sleep(30)
    #browser.quit()                                                         `   # (v.3.4 step 2)
    print('** Stop test_guest_can_add_product_to_basket **, time = ' + str(time.time() - time_0))


# pytest -s -v test_product_page.py::test_guest_cant_see_success_message_after_adding_product_to_basket > log.log

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):       # (v.4.3 step 6)
    time_0 = time.time()
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Добавляем товар в корзину
    page.add_to_basket()
    # 4. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


# pytest -s -v test_product_page.py::test_guest_cant_see_success_message > log.log

def test_guest_cant_see_success_message(browser):                                      # (v.4.3 step 6)
    time_0 = time.time()
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page.should_not_be_success_message()


# pytest -s -v test_product_page.py::test_message_disappeared_after_adding_product_to_basket > log.log

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):                  # (v.4.3 step 6)
    time_0 = time.time()
    # 1. Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес.
    page = ProductPage(browser, link)
    # 2. Открываем страницу товара
    page.open()
    # 3. Добавляем товар в корзину
    page.add_to_basket()
    # 4. Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page.should_be_disappeared_message()


# pytest -s -v test_product_page.py::test_guest_should_see_login_link_on_product_page > log.log
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    

# pytest -s -v test_product_page.py::test_guest_can_go_to_login_page_from_product_page > log.log
#@pytest.mark.need_review                                            # (v.4.3 step 14)
def test_guest_can_go_to_login_page_from_product_page(browser):                     # (v.4.3 step 8) (v.4.3 step 14) +++`
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)                                               # (v.4.3 step 11)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_login_page()


# pytest -s -v test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page > log.log
#@pytest.mark.need_review                                            # (v.4.3 step 14)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):        # (v.4.3 step 10) (v.4.3 step 14) +++
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    # 1. Гость открывает страницу товара                                                 # (v.4.3 step 10)
    page.open()
    # 2. Переходит в корзину по кнопке в шапке
    page.should_be_basket_link()
    page.go_to_basket_page()
    # 3. Ожидаем, что в корзине нет товаров
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_empty()
    # 4. Ожидаем, что есть текст о том что корзина пуста
    page_basket.should_be_text_that_basket_is_empty()

    

class TestUserAddToBasketFromProductPage():  # (v.4.3 step 13), (v.4.3 step 11)

    # Добавьте в класс фикстуру setup.
    @classmethod
    def setup_class(self):                                          # (v.3.4 step 2)
        print("\n** Start setup **")
        # открыть страницу регистрации;
        page = ProductPage(browser, self.link)
        page.open()
        self.browser = webdriver.Chrome()

    #зарегистрировать нового пользователя;
    #проверить, что пользователь залогинен.
        
    def test_user_cant_see_success_message(self, browser):        # (v.4.3 step 13)
        time_0 = time.time()
        page = ProductPage(browser, self.link)

    @pytest.mark.need_review                                        # (v.4.3 step 14)
    def test_user_can_add_product_to_basket(self, browser):       # (v.4.3 step 13) +++ # (v.4.3 step 14)
        time_0 = time.time()
        page = ProductPage(browser, self.link)


    #Генерировать email адреса для пользователей можно по-разному, один из вариантов, чтобы избежать повторения, использовать текущее время с помощью модуля time:

    #import time # в начале файла

    #email = str(time.time()) + "@fakemail.org"
