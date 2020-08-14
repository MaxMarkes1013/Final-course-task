from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, ".btn-group>.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.NAME, "login-username")
    LOGIN_PASSWORD_FIELD = (By.NAME, "login-password")
    REGISTRATION_EMAIL_FIELD = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.NAME, "registration-password1")
    REGISTRATION_DOUBLE_PASSWORD_FIELD = (By.NAME, "registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class AddBusketLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_ITEM = (By.CSS_SELECTOR, ".alertinner>strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner>p>strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div>p.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert.alert-safe.alert-noicon.alert-success.fade.in")
    CLEAR_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p>a")
    CLEAR_BASKET = (By.CSS_SELECTOR, ".row>.col-sm-2>a>.thumbnail")
