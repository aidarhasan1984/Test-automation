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