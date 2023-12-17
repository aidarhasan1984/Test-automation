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