import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def open(self):
        self.browser.get(self.url)


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.BUTTON_SIGN_IN_OR_UP)
        link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_SIGN_IN_OR_UP), "Login link is not presented"


    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BASKET_LINK)
        link.click()


    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_VIEW_BASKET_LINK), "Basket link is not presented"


    # Проверяет, что пользователь залогинен:
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"


    # абстрактный метод, который проверяет, что элемент существует
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            self.browser.implicitly_wait(10)
        except NoSuchElementException:
            return False
        return True


    def solve_quiz_and_get_code(self):
        try:    # Модальное окно с заданием вычислить выражение от Х и ввести ответ в поле (решить задачу нужно за 3 сек):
            WebDriverWait(self.browser, 30).until(EC.alert_is_present())    # ждем пока не появится модальное окно
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            x = alert_text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except TimeoutException:
            print("No first alert presented!!!")
        try:    # Второе модальное окно с проверочным кодом для ответа
            alert = self.browser.switch_to.alert
            self.browser.implicitly_wait(30)                                # ждем пока не появится модальное окно
            alert_text = alert.text
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented!!!")


    # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=0.01):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    # абстрактный метод, который проверяет, что элемент исчезает в течение заданного времени: 
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    # Получает текст элемента
    def get_element_text(self, *arg):
        text = self.browser.find_element(*arg).text
        text = str(text.replace("\n", " "))     # обработка случая когда текст располагается на нескольких строках
        return text


    # преобразует строку содержащую цену и символ валюты в вещественное число
    def delete_currency_sign(self, line):
        line = str(line)
        signs = ['\xa3', '&#xa3', '&#163', '\x20bd', '&#x20bd', '&#8381', '\x24', '&#x24', '&#36']  # список символов валют
        for sign in signs:
            line = line.replace(sign, '')
        line = line.strip()
        line = line.replace(',', '.')
        return float(line)


class Product():
    def __init__(self, name, price = 0.0, amount = 0):
        self.name = str(name)
        self.price = float(price)
        self.amount = int(amount)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_amount(self, amount):
        self.amount = int(amount)

    def get_amount(self):
        return self.amount
