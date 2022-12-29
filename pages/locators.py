from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[href = '/en-gb/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form")
    ALERT_SUCCESS = (By.CSS_SELECTOR, \
            ".alert.alert-safe.alert-noicon.alert-success .alertinner strong")
    ALERT_INFO = (By.CSS_SELECTOR, \
            ".alert.alert-safe.alert-noicon.alert-info .alertinner strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".content .row .col-sm-6.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".content .row .col-sm-6.product_main p")
    
    
