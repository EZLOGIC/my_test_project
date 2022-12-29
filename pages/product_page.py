from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        login_link.click()
        self.solve_quiz_and_get_code()

    def should_be_alert_message(self):
        self.should_be_alert_success_message()
        self.should_be_alert_info_message()
        
    def should_be_alert_info_message(self):
        basket_total_message = self.browser.find_element(*ProductPageLocators.ALERT_INFO)
        basket_total = basket_total_message.text
        book_price_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price_message.text
        assert basket_total == book_price, "Should be equal prices"

    def should_be_alert_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS)
        success_message_book_name = success_message.text
        book_title_message = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        book_title = book_title_message.text
        assert success_message_book_name == book_title, "Should be equal book titles"
    
    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS),\
            "Success message is presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
           "Success message is presented, but should not be"
    
        
