from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from .flightdetails import FlightDetailsWidget


class ConfirmationPage:

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.departure_flight = FlightDetailsWidget(browser, parent_div_xpath="//div[@data-test-id='flight-review-0']")
        self.return_flight = FlightDetailsWidget(browser, parent_div_xpath="//div[@data-test-id='flight-review-1']")

    def get_departure_flight_info(self):
        return self.departure_flight.get_flight_info()

    def get_return_flight_info(self):
        return self.return_flight.get_flight_info()

    def get_price(self):
        return self.browser.find_element_by_xpath("//table[@data-test-id='trip-total']//span").text

    def wait_for_load(self):
        WebDriverWait(self.browser, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[@data-test-id='flight-review-0']")
            )
        )
