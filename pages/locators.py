from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

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
    
    
