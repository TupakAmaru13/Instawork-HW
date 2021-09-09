from datetime import datetime
from selenium import webdriver


class DateWidget:

    def __init__(self, browser: webdriver, start_date_input_id: str, end_date_input_id: str):
        self.browser = browser
        self.start_date_input_id = start_date_input_id
        self.end_date_input_id = end_date_input_id

    def _pick_date(self, input_id, date: datetime):
        already_picked_date = self.browser.find_element_by_xpath(f"//input[@id='{input_id}']").get_attribute('value')
        wanted_date = date.strftime("%Y-%m-%d")
        if already_picked_date != wanted_date:
            self._open_picker(input_id)
            self._click_on_date(date)
            self._click_done()

    def _open_picker(self, input_id):
        self.browser.find_element_by_xpath(f"//button[@data-name='{input_id}']").click()

    def _click_on_date(self, date: datetime):
        month_label = date.strftime("%B %Y")
        day_label = date.strftime("%-d")
        date_button = self.browser.find_element_by_xpath(
            f'//div[@data-stid="date-picker-month"][h2/text()="{month_label}"]//button[@data-day="{day_label}"]'
        )
        if 'selected' not in date_button.get_attribute('class').split():
            date_button.click()

    def _click_done(self):
        self.browser.find_element_by_xpath("//button[@data-stid='apply-date-picker']").click()

    def pick_date_range(self, start_date: datetime, end_date: datetime):
        # assumes that:
        # 1. the dates are within a month, so they will be displayed without scrolling
        # 2. the dates are valid (e.g. later than today)
        self._pick_date("d1", start_date)
        self._pick_date("d2", end_date)

    def get_start_date(self):
        return self.browser.find_element_by_id(self.start_date_input_id).get_attribute('value')

    def get_end_date(self):
        return self.browser.find_element_by_id(self.end_date_input_id).get_attribute('value')
