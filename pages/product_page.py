from .base_page import BasePage
from .locators import AddBusketLocators

class AddBasket(BasePage):
    def add_item_into_basket(self):
        button = self.browser.find_element(*AddBusketLocators.BASKET_BUTTON)
        button.click()

    def should_be_message_about_adding_to_basket(self):
        assert self.is_element_present(*AddBusketLocators.ITEM_NAME)
        assert self.is_element_present(*AddBusketLocators.MESSAGE_ITEM)
        message = self.browser.find_element(*AddBusketLocators.MESSAGE_ITEM).text
        item_name = self.browser.find_element(*AddBusketLocators.ITEM_NAME).text
        assert message == item_name, "Item name in the message about adding in the basket is incorrect"

    def should_be_basket_price_is_similar_to_item_price(self):
        assert self.is_element_present(*AddBusketLocators.ITEM_PRICE)
        assert self.is_element_present(*AddBusketLocators.BASKET_PRICE)
        price = self.browser.find_element(*AddBusketLocators.BASKET_PRICE).text
        item_price = self.browser.find_element(*AddBusketLocators.ITEM_PRICE).text
        assert price == item_price, "Price in the message about adding in the basket is incorrect"
