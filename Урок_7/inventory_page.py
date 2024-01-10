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