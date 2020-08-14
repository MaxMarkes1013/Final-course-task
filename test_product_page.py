from pages.product_page import AddBasket
from pages.base_page import BasePage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = AddBasket(browser, link)
    page.open()
    page.add_item_into_basket()
    page.solve_quiz_and_get_code()
    page.message_about_adding_to_basket()
    page.basket_price_is_similar_to_item_price()
