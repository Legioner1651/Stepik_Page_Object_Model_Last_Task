from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import LoginAndRegistrationLocators
from .locators import StoreLocators
from .locators import BasketLocators
#from .login_page import LoginPage
import time


#email = str(time.time()) + "@fakemail.org"      # (v.4.3 step 13)

# главная страница нашего приложения
class ProductPage(BasePage):            # (v.4.3 step 2)

#-    def go_to_login_page(self):
#-        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)    # Селектор берем из class ProductPageLocators()
#-        login_link.click()
#-        # return LoginPage(browser=self.browser, url=self.browser.current_url)
#-        login_page = LoginPage(browser, browser.current_url)
#-        login_page.should_be_login_page()
#-        alert = self.browser.switch_to.alert
#-        alert.accept()

# Описать в нем метод для добавления в корзину. # (v.4.3 step 2)
# Дописать методы-проверки.                     # (v.4.3 step 2)

    # проверка наличия кнопки "Добавить в корзину"
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET_LINK), "Button link is not presented" # Селектор берем из class ProductPageLocators()

    # нажатие на кнопку "Добавить в корзину"
    def click_on_the_button_add_to_basket(self):
        button_link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET_LINK)
        button_link.click()

    # метод добавления в корзину
    def add_to_basket(self):
        # проверить наличие кнопки "Добавить в корзину"
        self.should_be_basket_button()
        # нажатие на кнопку "Добавить в корзину"
        self.click_on_the_button_add_to_basket()
        # метод передающий рассчитанный проверочный код в первом алерте и выводящий на печать сообщение из второго алерта.
        self.solve_quiz_and_get_code()

    # Получаем название товара.
    def get_name_product(self, *arg):
        name = self.browser.find_element(*arg).text
        self.browser.implicitly_wait(10)
        print('name = "' + name + '"')
        return name

    # получаем цену товара.
    def get_price_product(self, *arg):
        price = self.browser.find_element(*arg).text
        self.browser.implicitly_wait(10)
        print('price = "' + str(price[1:]) + '"')
        return float(price[1:])

    def get_name_product_catalogue(self):
        return self.get_name_product(*ProductPageLocators.NAME_LINK)

    def get_name_product_basket(self):
        return self.get_name_product(*ProductPageLocators.CONFIRMATION_NAME_LINK)

    def get_price_product_catalogue(self):
        return self.get_price_product(*ProductPageLocators.PRICE_LINK)

    def get_price_product_basket(self):
        return self.get_price_product(*ProductPageLocators.BASKET_TOTAL_LINK)

    # получаем кортеж: наименование товара + цена
    def get_name_and_price_product(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_LINK).text
        self.browser.implicitly_wait(10)
        price = self.browser.find_element(*ProductPageLocators.PRICE_LINK).text
        self.browser.implicitly_wait(10)
        return (name, price)

    # проверка подтверждения успешного добавления товара в корзину
    def checking_of_confirmation_of_successful_addition(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_LINK), "Отсутствует строка с результатом добавленния товара"
        assert (' has been added to your basket.' in self.get_element_text(*ProductPageLocators.CONFIRMATION_LINK) or ' был добавлен в вашу корзину.' in self.get_element_text(*ProductPageLocators.CONFIRMATION_LINK)), "Отсутствует подтверждение о добавлении товара в корзину EN"

    # проверка подтверждения, что корзина соответствует условиям предложения «Deferred benefit offer»
    def checking_of_confirmation_of_deferred_benefit_offer(self):
        assert self.is_element_present(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK), "Отсутствует строка про активное предложение"
        assert ('Your basket now qualifies for the ' in self.get_element_text(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK) or 'Ваша корзина удовлетворяет условиям предложения ' in self.get_element_text(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK)), "Отсутствует подтверждение что корзина удовлетворяет условиям предложения"

    # проверка того что название товара не поменялось
    def checking_that_product_name_has_not_changed(self, product):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_NAME_LINK), "Отсутствует наименование добавленного товара"
        assert self.get_name_product_basket() == product.get_name(), "Наименование товара изменилось"

    # проверка того что цена не поменялась.
    def checking_that_price_has_not_changed(self, product):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_LINK), "Отсутствует стоимость корзины"
        assert self.get_price_product_basket() == product.get_price(), "Цена товара изменилось"

    # метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются похожим образом, мы будем называть их should_be_(название элемента)
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_SIGN_IN_OR_UP), "Login link is not presented" # Селектор берем из class ProductPageLocators()

    # False, если в течении выбранного промежутка времени появится искомый сообщение.
    def should_not_be_success_message(self):                    # (v.4.3 step 5)
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMATION_LINK),  "Success message is presented, but should not be"

    # False, если проверка что сообщение не исчезло в течении выбранного промежутка времени.
    def should_be_disappeared_message(self):                    # (v.4.3 step 5)    метод, который проверяет, что элемент исчезает в течение заданного времени
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_LINK), "Success message did not disappear, but should be"

    # False, если в течении выбранного промежутка времени искомый элемент не исчезнет
    def should_not_be_checkable_element(self):                    # ()
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_LINK), "Success element did not disappear, but should be"

#6. Добавьте в класс фикстуру setup. В этой функции нужно:      # (v.4.3 step 13)
#   открыть страницу регистрации;
#   зарегистрировать нового пользователя;
#   проверить, что пользователь залогинен.
