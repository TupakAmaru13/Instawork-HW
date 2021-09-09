from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from .location import LocationWidget
from .datepicker import DateWidget
from .flightdetails import FlightDetailsWidget


class FlightsResultsPage:

    first_flight_li_xpath = "//ul[@data-test-id='listings']/li[1]//button"

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.origin = LocationWidget(browser, "typeahead-originInput-0")
        self.destination = LocationWidget(browser, "typeahead-destinationInput-0")
        self.date_picker = DateWidget(browser, "start-date-ROUND_TRIP-0", "end-date-ROUND_TRIP-0")

    def get_origin(self) -> str:
        return self.origin.get_value()

    def get_destination(self) -> str:
        return self.destination.get_value()

    def get_departure_date(self):
        return self.date_picker.get_start_date()

    def get_return_date(self):
        return self.date_picker.get_end_date()

    def select_nonstop(self):
        self.browser.find_element_by_id("stops-0").click()
        self.wait_for_results()

    def sort_results_by_price_desc(self):
        sort_dropdown = Select(self.browser.find_element_by_id("listings-sort"))
        sort_dropdown.select_by_value("PRICE_DECREASING")
        self.wait_for_results()

    def select_first_flight(self):
        self.browser.find_element_by_xpath(FlightsResultsPage.first_flight_li_xpath).click()

    def confirm_flight_selection(self):
        self.browser.find_element_by_xpath("//button[@data-test-id='select-button']").click()

    def get_expected_price(self):
        # assumes the flight details slider is opened
        expected_price = self.browser.find_element_by_xpath(
            "//div[@data-test-id='listing-details-and-fares']//div[@data-test-id='details-and-fares-footer']//span[@class='uitk-lockup-price']"
        ).text
        return expected_price

    def get_selected_flight_info(self):
        # assumes the flight details slider is opened
        return FlightDetailsWidget(self.browser, "//div[@data-test-id='details-and-fares']").get_flight_info()

    def wait_for_results(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.element_to_be_clickable((By.XPATH, FlightsResultsPage.first_flight_li_xpath))
        )


