class CartPage:
    def __init__(self, browser):
        self.browser = browser

    def checkout(self):
        self.browser.find_element_by_id("checkout").click()