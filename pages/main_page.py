from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasePageLocators  # (v.4.2 step 7)
from .locators import LoginPageLocators
from .login_page import LoginPage # (v.4.2 step 9)



# главная страница нашего приложения
class MainPage(BasePage):           # (v.4.2 step 3)
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    #def go_to_login_page(self):     # (v.4.2 step 3) переход на страницу логина
        #login_link = self.browser.find_element(*BasePageLocators.BUTTON_SIGN_IN_OR_UP)    # Селектор берем из class MainPageLocators()  # (v.4.2 step 7)
        #login_link.click()          # (v.4.2 step 3)
        # return LoginPage(browser=self.browser, url=self.browser.current_url) # (v.4.2 step 9) + (v.4.2 step 9) Первый способ: возвращать нужный Page Object
        # обработка alert, который вызывается при клике на нужную нам ссылку (если нужно):
        # alert = self.browser.switch_to.alert        # (v.4.2 step 10)
        # alert.accept()                              # (v.4.2 step 10)

    # метод, который будет проверять наличие ссылки. Обычно все такие методы-проверки называются похожим образом, мы будем называть их should_be_(название элемента)
    # проверяем что существует страница по указанной ссылке.
    # should_be_(название элемента) -  метод, который будет проверять наличие ссылки (v.4.2 step 5)
    #def should_be_login_link(self):   # (v.4.2 step 5) - Проверка, что есть ссылка, которая ведет на логин
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid") # (v.4.2 step 5)
        #assert self.is_element_present(*BasePageLocators.BUTTON_SIGN_IN_OR_UP), "Login link is not presented" # Селектор берем из class MainPageLocators() # (v.4.2 step 6) + (v.4.2 step 7)
