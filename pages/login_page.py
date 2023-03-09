from .base_page import BasePage
from .locators import LoginAndRegistrationLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, "Current URL и отсутствует подстрока 'login'"
        assert current_url == self.url, "Current URL !=  URL in BasePage"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_EMAIL_LINK), "Отсутствует поле ввода email"
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_PASSWORD_LINK), "Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.LOGIN_BUTTON_LINK), "Отсутствует кнопка входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_EMAIL_LINK), "Отсутствует поле ввода email"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_PASSWORD1_LINK), "Отсутствует поле ввода пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_PASSWORD2_LINK), "Отсутствует поле ввода подтверждения пароля"
        assert self.is_element_present(*LoginAndRegistrationLocators.REGISTER_BUTTON_LINK), "Отсутствует кнопка регистрации"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        email_link = self.browser.find_element(*LoginAndRegistrationLocators.REGISTER_EMAIL_LINK)
        email_link.send_keys(email)
        password1_link = self.browser.find_element(*LoginAndRegistrationLocators.REGISTER_PASSWORD1_LINK)
        password1_link.send_keys(password)
        password2_link = self.browser.find_element(*LoginAndRegistrationLocators.REGISTER_PASSWORD2_LINK)
        password2_link.send_keys(password)
        button_link = self.browser.find_element(*LoginAndRegistrationLocators.REGISTER_BUTTON_LINK)
        button_link.click()
