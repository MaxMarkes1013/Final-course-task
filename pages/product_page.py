from .base_page import BasePage
from .locators import AddBusketLocators

class AddBasket(BasePage):
    def add_item_into_basket(self):
        button = self.browser.find_element(*AddBusketLocators.BASKET_BUTTON)
        button.click()

    def message_about_adding_to_basket(self):
        message = self.browser.find_element(*AddBusketLocators.MESSAGE_ITEM)
        assert "The shellcoder's handbook" in message.text, "Item name in the message about adding in the basket is incorrect"

    def basket_price_is_similar_to_item_price(self):
        price = self.browser.find_element(*AddBusketLocators.BASKET_PRICE)
        assert "9,99 £" in price.text, "Price in the message about adding in the basket is incorrect"
