class SummaryPage:
    def __init__(self, browser):
        self.browser = browser

    def get_total(self):
        return self.browser.find_element_by_class_name("summary_total_label").text