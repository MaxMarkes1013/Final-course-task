from pages.product_page import AddBasket
from pages.base_page import BasePage
import time
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = AddBasket(browser, link)
    page.open()
    page.add_item_into_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_to_basket()
    page.should_be_basket_price_is_similar_to_item_price()
