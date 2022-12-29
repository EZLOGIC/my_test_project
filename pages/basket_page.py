from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), "Should not be items"
        
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), "Should be empty"
