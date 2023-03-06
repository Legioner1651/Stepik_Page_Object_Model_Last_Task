# сделаем базовую страницу, от которой будут унаследованы все остальные классы.
# В ней мы опишем вспомогательные методы для работы с драйвером.
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException   # (v.4.2 step 6)
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):           # (v.4.2 step 6)    в качестве параметров мы передаем экземпляр драйвера и url адрес и неявного ожидания со значением по умолчанию в 10
        self.browser = browser                              # (v.4.2 step 2)
        self.url = url                                      # (v.4.2 step 2)
        self.browser.implicitly_wait(timeout)               # (v.4.2 step 6)    неявного ожидания со значением по умолчанию в 10
        #self.product={}
        #self.last_add_product = None
        #self.name = ""      # наименование товара   (str)
        #self.price = 0.0    # цена товара           (float)
        #self.amount = 0     # количество товара     (int)


    def open(self):  # метод open, открывает нужную страницу в браузере, используя метод get() (v.4.2 step 2)
        self.browser.get(self.url)


    def go_to_login_page(self):                             # (v.4.2 step 3)    # (v.4.3 step 8)
        link = self.browser.find_element(*BasePageLocators.BUTTON_SIGN_IN_OR_UP)
        link.click()


    # should_be_(название элемента) -  метод, который будет проверять наличие ссылки (v.4.2 step 5)
    def should_be_login_link(self):                         # (v.4.2 step 5)    # (v.4.3 step 8)
        assert self.is_element_present(*BasePageLocators.BUTTON_SIGN_IN_OR_UP), "Login link is not presented"


    def go_to_basket_page(self):                             # (v.4.3 step 10)
        link = self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BASKET_LINK)
        link.click()


    def should_be_basket_link(self):                         # (v.4.2 step 5)    # (v.4.3 step 8)
        assert self.is_element_present(*BasePageLocators.BUTTON_VIEW_BASKET_LINK), "Basket link is not presented"


    def is_element_present(self, how, what):  # how селектор, what - ссылка  # (v.4.2 step 6)
        try:                                                # (v.4.2 step 6)
            self.browser.find_element(how, what)            # (v.4.2 step 6)
        except NoSuchElementException:                      # (v.4.2 step 6)
            return False                                    # (v.4.2 step 6)
        return True                                         # (v.4.2 step 6)


    def solve_quiz_and_get_code(self):                              # (v.4.3 step 2)
        time_0 = time.time()
        print('**** Start metod "solve_quiz_and_get_code" **** ', time.time() - time_0)
        try:    # Модальное окно с заданием вычислить выражение от Х и ввести ответ в поле (решить задачу нужно за 3 сек):
            print('time start 1 try', time.time() - time_0)
            WebDriverWait(self.browser, 30).until(EC.alert_is_present())   # ждем пока не появится модальное окно
            alert = self.browser.switch_to.alert                    # (v.4.3 step 2)
            print('time switch_to.alert 1 try', time.time() - time_0)
            alert_text = alert.text
            print('\nfirst alert.text: \n' + alert_text + '\n')
            x = alert_text.split(" ")[2]                            # (v.4.3 step 2)
            answer = str(math.log(abs((12 * math.sin(float(x))))))  # (v.4.3 step 2)
            alert.send_keys(answer)                                 # (v.4.3 step 2)
            #time.sleep(30)                                          # для тестирования
            alert.accept()                                          # (v.4.3 step 2)
            print('answer = ' + answer)
            print('time end 1 try', time.time() - time_0)
        except TimeoutException:
            print("No first alert presented!!!")
        try:    # Второе модальное окно с проверочным кодом для ответа          # (v.4.3 step 2)
            print('time start 2 try', time.time() - time_0)
            alert = self.browser.switch_to.alert                    # (v.4.3 step 2)
            self.browser.implicitly_wait(30)
            print('time switch_to.alert 2 try', time.time() - time_0)
            alert_text = alert.text                                 # (v.4.3 step 2)
            print('\nsecond alert.text:\n' + f"Your code: {alert_text}" + '\n')                       # (v.4.3 step 2)
            #time.sleep(10)                                          # для тестирования
            alert.accept()                                          # (v.4.3 step 2)
            print('time end 2 try', time.time() - time_0)
        except NoAlertPresentException:                             # (v.4.3 step 2)
            print("No second alert presented!!!")                      # (v.4.3 step 2)
        print('**** End metod "solve_quiz_and_get_code" **** ', time.time() - time_0)


    # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=0.01):         # (v.4.3 step 5)
        try:                                                        # (v.4.3 step 5)
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:                                    # (v.4.3 step 5)
            return True                                             # (v.4.3 step 5)

        return False                                                # (v.4.3 step 5)


    # абстрактный метод, который проверяет, что элемент исчезает в течение заданного времени: 
    def is_disappeared(self, how, what, timeout=4):                 # (v.4.3 step 5)
        try:                                                        # (v.4.3 step 5)
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:                                    # (v.4.3 step 5)
            return False                                            # (v.4.3 step 5)

        return True                                                 # (v.4.3 step 5)


    def get_element_text(self, *arg):
        text = self.browser.find_element(*arg).text
        text = str(text.replace("\n", " "))     # обработка случая когда текст располагался на нескольких строках
        return text


    # абстрактный метод, который проверяет, что пользователь залогинен:
    def should_be_authorized_user(self):                                                                                            # (v.4.3 step 13)
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," " probably unauthorised user"    # (v.4.3 step 13)


    def add_product(self, name, price, amount = 1):     # ????????
        if name not in self.product.keys():
            self.product[name] = [[price for i in range(amount)], amount]
            self.last_add_product = name
        else:
            self.product[name][0].extend([price for i in range(amount)])
            self.product[name][1] += amount
            self.last_add_product = name


    def del_product(self, name, price, amount):         # ????????
        if name in self.product.keys() and self.product[name][1] >= amount:     # product with name is present and amount enough for delete
            count = 0
            for value in self.product[name][0]:
                if value == price:
                    count +=1
            if count == amount == self.product[name][1]:                        # amount == the remainder => delete all with this name
                self.product.pop(name)
            elif count > amount:                                                # amount < the remainder
                for idx in range(amount):
                    self.product[name][0].remove(price)
                self.product[name][1] -= amount
            else:
                print ('Error: Delete operation failed, there are not so many elements with the right price')
        else:
            print ('Error: Delete operation failed, there are not so many elements')


    def get_last_name_product(self):
        return self.last_add_product


    def get_lst_price_product(self, name):          # receive list of prices
        return self.product[name][0]


    def get_amount_product(self, name):
        return self.product[name][1]
    

    def print_product(self):
        print(self.product)


class Product():                # Товар
    def __init__(self, name, price = 0.0, amount = 0):
        self.name = str(name)       # (str)
        self.price = float(price)   # (float)
        self.amount = int(amount)   # (int)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount
