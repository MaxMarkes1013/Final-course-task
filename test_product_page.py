from pages.product_page import AddBasket
from pages.base_page import BasePage
from pages.basket_page import Basket
from pages.login_page import LoginPage
import pytest
import time

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddBasket(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddBasket(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = AddBasket(browser, link)
    page.open()
    page.add_item_into_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_to_basket()
    page.should_be_basket_price_is_similar_to_item_price()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer%7Bpromo_offer"
    page = AddBasket(browser, link)
    page.open()
    page.add_item_into_basket()
    page.solve_quiz_and_get_code()
    page.should_not_disappear_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer%7Bpromo_offer"
    page = AddBasket(browser, link)
    page.open()
    page.add_item_into_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_user_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = Basket(browser, link)
    page.open()
    page.should_open_basket()
    page.should_be_clear_basket
    page.should_be_message_about_clear_basket()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@ffffffmail.com"
        password = "497952727589372589325890"
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer%7Bpromo_offer"
        page = AddBasket(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_user_can_add_product_to_basket(self, browser, promo_offer):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = AddBasket(browser, link)
        page.open()
        page.add_item_into_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding_to_basket()
        page.should_be_basket_price_is_similar_to_item_price()
