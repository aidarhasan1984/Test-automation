class FormPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def fill_form(self, first_name, last_name, address, email, phone, city, country, job_position, company):
        self.browser.find_element_by_name("first-name").send_keys(first_name)
        self.browser.find_element_by_name("last-name").send_keys(last_name)
        self.browser.find_element_by_name("address").send_keys(address)
        self.browser.find_element_by_name("e-mail").send_keys(email)
        self.browser.find_element_by_name("phone").send_keys(phone)
        self.browser.find_element_by_name("city").send_keys(city)
        self.browser.find_element_by_name("country").send_keys(country)
        self.browser.find_element_by_name("job-position").send_keys(job_position)
        self.browser.find_element_by_name("company").send_keys(company)

    def submit_form(self):
        self.browser.find_element_by_css_selector(".btn.btn-outline-primary.mt-3").click()

    def is_zip_code_highlighted_red(self):
        zip_code_field = self.browser.find_element_by_name("zip-code")
        return "border-color: red" in zip_code_field.get_attribute("outerHTML")

    def are_other_fields_highlighted_green(self):
        fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        for field in fields:
            element = self.browser.find_element_by_name(field)
            if "border-color: green" not in element.get_attribute("outerHTML"):
                return False
        return True