from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketLocators
#from .login_page import LoginPage



# главная страница нашего приложения
class BasketPage(BasePage):             # (v.4.3 step 10)

    # В классе BasePage реализуйте соответствующий метод для перехода в корзину.      # (v.4.3 step 10)
    # Создайте файл basket_page.py и в нем класс BasketPage.
    # Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах.

    def should_be_basket_button(self):    #?????
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BUTTON_BASKET_LINK), "Button link is not presented" # Селектор берем из class ProductPageLocators()


    def should_be_empty(self):                         # (v.4.3 step 10)
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET_LINK), "Basket is not empty"


    # Ожидаем, что есть текст о том что корзина пуста
    def should_be_text_that_basket_is_empty(self):
        assert ('Your basket is empty' in self.get_element_text(*BasketLocators.EMPTY_BASKET_LINK) or 'Ваша корзина пуста' in self.get_element_text(*BasketLocators.EMPTY_BASKET_LINK)), "Отсутствует текст что корзина пуста"


    # Проверяем, что в корзине не появились товары
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.LIST_OF_ITEMS_IN_BASKET), "Product is presented, but should not be"
