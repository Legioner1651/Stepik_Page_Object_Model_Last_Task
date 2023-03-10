from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # проверка наличия кнопки "Добавить в корзину"
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BASKET_LINK), "Button link is not presented"


    # нажатие на кнопку "Добавить в корзину"
    def click_on_the_button_add_to_basket(self):
        button_link = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET_LINK)
        button_link.click()


    # метод добавления в корзину
    def add_to_basket(self):
        # проверить наличие кнопки "Добавить в корзину"
        self.should_be_basket_button()
        # нажать на кнопку "Добавить в корзину"
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
        price = self.delete_currency_sign(price)
        return price


    def get_name_product_catalogue(self):
        return self.get_name_product(*ProductPageLocators.NAME_LINK)


    def get_name_product_basket(self):
        return self.get_name_product(*ProductPageLocators.CONFIRMATION_NAME_LINK)


    def get_price_product_catalogue(self):
        return self.get_price_product(*ProductPageLocators.PRICE_LINK)


    def get_price_product_basket(self):
        return self.get_price_product(*ProductPageLocators.BASKET_TOTAL_LINK)


    # проверка подтверждения успешного добавления товара в корзину
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_LINK), "Отсутствует строка с результатом добавления товара"
        assert (' has been added to your basket.' in self.get_element_text(*ProductPageLocators.CONFIRMATION_LINK) or ' был добавлен в вашу корзину.' in self.get_element_text(*ProductPageLocators.CONFIRMATION_LINK)), "Отсутствует подтверждение о добавлении товара в корзину EN"


    # проверка подтверждения, что корзина соответствует условиям предложения «Deferred benefit offer»
    def should_be_message_success_accordance(self):
        assert self.is_element_present(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK), "Отсутствует строка про активное предложение"
        assert ('Your basket now qualifies for the ' in self.get_element_text(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK) or 'Ваша корзина удовлетворяет условиям предложения ' in self.get_element_text(*ProductPageLocators.OFFER_DEFERRED_BENEFIT_LINK)), "Отсутствует подтверждение что корзина удовлетворяет условиям предложения"


    # проверка того что название товара не поменялось
    def should_be_name_added_product(self, product):
        assert self.is_element_present(*ProductPageLocators.CONFIRMATION_NAME_LINK), "Отсутствует наименование добавленного товара"
        assert self.get_name_product_basket() == product.get_name(), "Наименование товара изменилось"


    # проверка того что цена не поменялась.
    def should_be_equal_price_added_product(self, product):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_LINK), "Отсутствует стоимость корзины"
        assert self.get_price_product_basket() == product.get_price(), "Цена товара изменилось"


    # метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются похожим образом, мы будем называть их should_be_(название элемента)
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_SIGN_IN_OR_UP), "Login link is not presented"


    # False, если в течении выбранного промежутка времени появится искомый сообщение.
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRMATION_LINK),  "Success message is presented, but should not be"


    # False, если проверка что сообщение не исчезло в течении выбранного промежутка времени.
    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_LINK), "Success message did not disappear, but should be"


    # False, если в течении выбранного промежутка времени искомый элемент не исчезнет
    def should_not_be_checkable_element(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRMATION_LINK), "Success element did not disappear, but should be"
