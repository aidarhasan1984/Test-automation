import pytest
from selenium import webdriver

@pytest.fixture
def browser():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver

    driver.quit()

def test_fill_form_and_check_highlight(browser):
    
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    
    first_name_input = browser.find_element_by_name("first-name")
    first_name_input.send_keys("Иван")

    last_name_input = browser.find_element_by_name("last-name")
    last_name_input.send_keys("Петров")

    address_input = browser.find_element_by_name("address")
    address_input.send_keys("Ленина, 55-3")

    email_input = browser.find_element_by_name("e-mail")
    email_input.send_keys("test@skypro.com")

    phone_input = browser.find_element_by_name("phone")
    phone_input.send_keys("+7985899998787")

    city_input = browser.find_element_by_name("city")
    city_input.send_keys("Москва")

    country_input = browser.find_element_by_name("country")
    country_input.send_keys("Россия")

    job_position_input = browser.find_element_by_name("job-position")
    job_position_input.send_keys("QA")

    company_input = browser.find_element_by_name("company")
    company_input.send_keys("SkyPro")

    submit_button = browser.find_element_by_css_selector(".btn.btn-outline-primary.mt-3")
    submit_button.click()

    zip_code_input = browser.find_element_by_name("zip-code")
    assert "border-danger" in zip_code_input.get_attribute("class")

    other_inputs = [
        first_name_input, last_name_input, address_input, email_input,
        phone_input, city_input, country_input, job_position_input, company_input
    ]
    for input in other_inputs:
        assert "border-success" in input.get_attribute("class")