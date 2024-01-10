import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from summary_page import SummaryPage

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