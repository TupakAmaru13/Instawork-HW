from behave import step, then, when
from selenium import webdriver
from datetime import datetime, timedelta
from time import sleep


@step("Navigate to Orbitz")
def navigate_to_orbitz(context):
    context.browser.get("https://orbitz.com")


@step("Select Flights")
def select_flights(context):
    MainPage(context.browser).select_flights()


@step("Select Roundtrip")
def select_roundtrip(context):
    MainPage(context.browser).select_roundtrip()


@step("Leave from {origin}")
def leave_from(context, origin: str):
    MainPage(context.browser).origin.type_destination_and_select_first(origin)


@step("Fly to {destination}")
def fly_to(context, destination: str):
    MainPage(context.browser).destination.type_destination_and_select_first(destination)


@step("Depart 2 weeks from today and return 3 weeks from today")
def fly_on_date_range(context):
    today = datetime.today()
    start_date = today + timedelta(days=14)
    end_date = today + timedelta(days=21)
    MainPage(context.browser).date_picker.pick_date_range(start_date, end_date)


@step("Search")
def search(context):
    MainPage(context.browser).search()


@then("Something")
def something(context):
    print("XXXXXXXXXXXXXXXXX")


class MainPage:
    flights_xpath = "//a[@aria-controls='wizard-flight-pwa']"
    roundtrip_xpath = "//a[@aria-controls='wizard-flight-tab-roundtrip']"

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.origin = LocationWidget(browser, "location-field-leg1-origin")
        self.destination = LocationWidget(browser, "location-field-leg1-destination")
        self.date_picker = DateWidget(browser, "d1")
        self.search_button_xpath = "//button[@data-testid='submit-button']"

    def select_flights(self):
        self.browser.find_element_by_xpath(MainPage.flights_xpath).click()

    def select_roundtrip(self):
        self.browser.find_element_by_xpath(MainPage.roundtrip_xpath).click()

    def pick_dates(self, start_date: datetime, end_date):
        self.date_picker.pick_date_range(start_date, end_date)

    def search(self):
        self.browser.find_element_by_xpath(self.search_button_xpath).click()


class LocationWidget:

    def __init__(self, browser: webdriver, base_name: str):
        self.base_name = base_name
        self.browser = browser
        self.button_xpath = f'//button[@data-stid="{base_name}-menu-trigger"]'
        self.input_xpath = f'//input[@data-stid="{base_name}-menu-input"]'
        self.first_result_xpath = f'//ul[@data-stid="{base_name}-results"]/li[1]/button'

    def type_destination_and_select_first(self, destination: str):
        self.browser.find_element_by_xpath(self.button_xpath).click()
        self.browser.find_element_by_xpath(self.input_xpath).send_keys(destination)
        self.browser.find_element_by_xpath(self.first_result_xpath).click()


class DateWidget:

    def __init__(self, browser: webdriver, base_name: str):
        self.browser = browser
        self.base_name = base_name
        self.start_date_input_id = "d1"
        self.end_date_input_id = "d2"
        # self.start_date_trigger_button_xpath = f"//button[@data-name='{base_name}']"
        # self.end_date_trigger_button_xpath = f"//button[@data-name='{base_name}']"

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
