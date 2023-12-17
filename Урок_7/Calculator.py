import time

class SlowCalculatorPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def enter_delay(self, value):
        delay_input = self.browser.find_element_by_id("delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button_7(self):
        self.browser.find_element_by_xpath("//span[text()='7']").click()

    def click_button_plus(self):
        self.browser.find_element_by_xpath("//span[text()='+']").click()

    def click_button_8(self):
        self.browser.find_element_by_xpath("//span[text()='8']").click()

    def click_button_equals(self):
        self.browser.find_element_by_xpath("//span[text()='=']").click()

    def get_result_after_45_seconds(self):
        time.sleep(45)
        return self.browser.find_element_by_id("result").text