from .base_page import BasePage
from .locators import AddBusketLocators

class Basket(BasePage):
    def should_be_message_about_clear_basket(self):
        clear_basket_message = self.browser.find_element(*AddBusketLocators.CLEAR_BASKET_MESSAGE)
        assert clear_basket_message, "Basket message is not shown, but it should be"

    def should_be_clear_basket(self):
        assert self.is_not_element_present(*AddBusketLocators.CLEAR_BASKET), "Basket is not clear, but it should be"
