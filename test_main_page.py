from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
#from selenium.webdriver.common.by import By

# pytest -s -v test_main_page.py > log.log
# pytest -v --tb=line --language=en test_main_page.py > log.log

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"  # (v.4.3 step 2)
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
#link = "http://selenium1py.pythonanywhere.com/"

# pytest -s -v test_main_page.py::test_guest_can_go_to_login_page > log.log
def test_guest_can_go_to_login_page(browser):      # (v.4.1 step 6)(v.4.2 step 4)?
    #link = "http://selenium1py.pythonanywhere.com/"                   # (v.4.1 step 6)
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу  (v.4.2 step 4)
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина (v.4.2 step 4), (v.4.2 step 9)
    # login_page = page.go_to_login_page()  # (v.4.2 step 9)
    # login_page.should_be_login_page()  # (v.4.2 step 9)
    login_page = LoginPage(browser, browser.current_url)  # (v.4.2 step 9)
    login_page.should_be_login_page()                     # (v.4.2 step 9)
    # 4.1 step 6:
    #browser.get(link)                                                  # (v.4.1 step 6)
    #login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")  # (v.4.1 step 6)
    #login_link.click()                                                 # (v.4.1 step 6)
    # команда проверки работоспособности теста: pytest -v --tb=line --language=en test_main_page.py   # (v.4.1 step 6)  --tb=line, которая указывает, что нужно выводить только одну строку из лога каждого упавшего теста.


def test_guest_should_see_login_link(browser):  # (v.4.2 step 5) будет проверять наличие ссылки
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)              # (v.4.2 step 5)
    page.open()                                 # (v.4.2 step 5)
    page.should_be_login_link()                 # (v.4.2 step 5) - Проверка, что есть ссылка, которая ведет на логин
    

# 4.1 step 8: Запишем основные сценарии:        # (v.4.1 step 8)
# добавить в корзину; (test_add_to_cart)
# добавить в корзину товар с определенным названием   # (v.4.1 step 9)
# проверить, что есть сообщение об успешном добавлении в корзину;
# перейти к написанию отзыва;
# проверить, что есть название, цена, описание товара;
# вернуться на главную.
# перейти на следующую страницу списка товаров        # (v.4.1 step 9)
# перейти на страницу товара                          # (v.4.1 step 9)
# поменять язык интерфейса                            # (v.4.1 step 9)

# Примерно как должен выглядить кейс:
#def test_add_to_cart(browser):                                                                 # (v.4.1 step 8)
#    page = ProductPage(url="", browser)   # инициализируем объект Page Object                  # (v.4.1 step 8)
#    page.open()                           # открываем страницу в браузере                      # (v.4.1 step 8)
#    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину     # (v.4.1 step 8)
#    page.add_product_to_cart()            # жмем кнопку добавить в корзину                     # (v.4.1 step 8)
#    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом      # (v.4.1 step 8)


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
