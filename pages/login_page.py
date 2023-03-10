from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        registration_email.send_keys(email)
        registration_password1 = self.browser.find_element(*LoginPageLocators.PASSWORD)
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        registration_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER)
        register_button.click()
        
