from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not present in url"

    def should_be_login_form(self):
        login_email_field = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_FIELD)
        login_password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_FIELD)
        # реализуйте проверку, что есть форма логина
        assert True, "Login form is not present on the page"

    def should_be_register_form(self):
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        registration_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        registration_double_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_DOUBLE_PASSWORD_FIELD)
        # реализуйте проверку, что есть форма регистрации на странице
        assert True, "Register form is not present on the page"

    def register_new_user(self, email, password):
        registration_email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        registration_email_field.send_keys(email)
        registration_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        registration_password_field.send_keys(password)
        registration_double_password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_DOUBLE_PASSWORD_FIELD)
        registration_double_password_field.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()