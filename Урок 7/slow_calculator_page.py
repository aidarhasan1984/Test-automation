from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SlowCalculatorPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def enter_delay(self, value):
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button_7(self):
        self.browser.find_element(By.XPATH, "//span[text()='7']").click()

    def click_button_plus(self):
        self.browser.find_element(By.XPATH, "//span[text()='+']").click()

    def click_button_8(self):
        self.browser.find_element(By.XPATH, "//span[text()='8']").click()

    def click_button_equals(self):
        self.browser.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result_after_45_seconds(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located((By.ID, "result")))
        return self.browser.find_element(By.ID, "result").text