import pytest
from selenium import webdriver
from form_page import FormPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form_and_submit(browser):
    page = FormPage(browser)
    page.open("http://example.com/form")
    page.fill_form("John", "Doe", "123 Street", "john.doe@example.com", "1234567890", "City", "Country", "Manager", "ABC Inc.")
    page.submit_form()
    assert not page.is_zip_code_highlighted_red()
    assert page.are_other_fields_highlighted_green()