import pytest
from selenium import webdriver
from slow_calculator_page import SlowCalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    page = SlowCalculatorPage(browser)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page.enter_delay(45)
    page.click_button_7()
    page.click_button_plus()
    page.click_button_8()
    page.click_button_equals()
    result = page.get_result_after_45_seconds()
    assert result == "15"