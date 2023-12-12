import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_shopping_flow():
    
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    username = driver.find_element_by_id("user-name")
    password = driver.find_element_by_id("password")
    login_button = driver.find_element_by_id("login-button")
    
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()

    add_backpack = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
    add_tshirt = driver.find_element_by_id("add-to-cart-sauce-labs-bolt-t-shirt")
    add_onesie = driver.find_element_by_id("add-to-cart-sauce-labs-onesie")

    add_backpack.click()
    add_tshirt.click()
    add_onesie.click()

    shopping_cart = driver.find_element_by_class_name("shopping_cart_link")
    shopping_cart.click()

    checkout_button = driver.find_element_by_id("checkout")
    checkout_button.click()

    first_name = driver.find_element_by_id("first-name")
    last_name = driver.find_element_by_id("last-name")
    postal_code = driver.find_element_by_id("postal-code")
    continue_button = driver.find_element_by_id("continue")

    first_name.send_keys("Aidar")
    last_name.send_keys("Khasanov")
    postal_code.send_keys("480000")
    continue_button.click()

    total_price = driver.find_element_by_class_name("summary_total_label").text

    driver.quit()

    assert total_price == "Total: $58.29"

test_shopping_flow()