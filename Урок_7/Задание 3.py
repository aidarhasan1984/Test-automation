class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def login_as_standard_user(self, username, password):
        username_input = self.browser.find_element_by_id("user-name")
        password_input = self.browser.find_element_by_id("password")
        login_button = self.browser.find_element_by_id("login-button")

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

class InventoryPage:
    def __init__(self, browser):
        self.browser = browser

    def add_backpack_to_cart(self):
        self.browser.find_element_by_id("add-to-cart-sauce-labs-backpack").click()

    def add_bolt_tshirt_to_cart(self):
        self.browser.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie_to_cart(self):
        self.browser.find_element_by_id("add-to-cart-sauce-labs-onesie").click()

    def go_to_shopping_cart(self):
        self.browser.find_element_by_class_name("shopping_cart_link").click()

class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.browser.find_element_by_id("checkout").click()

class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_form(self, first_name, last_name, postal_code):
        first_name_input = self.browser.find_element_by_id("first-name")
        last_name_input = self.browser.find_element_by_id("last-name")
        postal_code_input = self.browser.find_element_by_id("postal-code")
        continue_button = self.browser.find_element_by_id("continue")

        first_name_input.clear()
        first_name_input.send_keys(first_name)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)
        continue_button.click()

class SummaryPage:
    def __init__(self, browser):
        self.browser = browser

    def get_total(self):
        return self.browser.find_element_by_class_name("summary_total_label").text
import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage, SummaryPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_sauce_demo_checkout(browser):
    login_page = LoginPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)
    checkout_page = CheckoutPage(browser)
    summary_page = SummaryPage(browser)

    login_page.open("https://www.saucedemo.com/")
    login_page.login_as_standard_user("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bolt_tshirt_to_cart()
    inventory_page.add_onesie_to_cart()
    
    inventory_page.go_to_shopping_cart()
    
    cart_page.checkout()
    
    checkout_page.fill_form("Aidar", "Khasanov", "480000")
    
    assert summary_page.get_total() == "Total: $58.29"