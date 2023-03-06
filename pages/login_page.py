# файл скачан по ссылке # (v.4.2 step 8)    https://stepik.org/media/attachments/lesson/199980/login_page.py
from .base_page import BasePage
from .locators import LoginAndRegistrationLocators


# метод, который будет проверять наличие ссылки.
# Обычно все такие методы-проверки называются похожим образом,
# мы будем называть их should_be_(название элемента)
class LoginPage(BasePage):                    # (v.4.2 step 8)
    
    def should_be_login_page(self):           # (v.4.2 step 8)
        self.should_be_login_url()            # (v.4.2 step 8)
        self.should_be_login_form()           # (v.4.2 step 8)
        self.should_be_register_form()        # (v.4.2 step 8)

    def should_be_login_url(self):            # (v.4.2 step 8)
        # реализуйте проверку на корректный url адрес
        # В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера. Для этого используйте соответствующее свойство Webdriver (v.4.2 step 8)
        current_url = self.browser.current_url   # Gets the URL of the current page
        assert 'login' in current_url, "Current URL итсутствует подстрока 'login'"
        assert current_url == self.url, "Current URL !=  URL in BasePage"

    def should_be_login_form(self):            # (v.4.2 step 8)
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_EMAIL_LINK), "Отсутствует поле ввода email"        # find_element
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_PASSWORD_LINK), "Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_BUTTON_LINK), "Отсутствует кнопка ввхода"

    def should_be_register_form(self):         # (v.4.2 step 8)
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_EMAIL_LINK), "Отсутствует поле ввода email"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_PASSWORD1_LINK), "Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_PASSWORD2_LINK), "Отсутствует поле ввода подтверждения пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_BUTTON_LINK), "Отсутствует кнопка регистрацииа"

#    def register_new_user(email, password):     # (v.4.3 step 13)   принимает две строки и регистрирует пользователя
#        Реализуйте его, описав соответствующие элементы страницы.
