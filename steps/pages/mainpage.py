from datetime import datetime
from selenium import webdriver
from .location import LocationWidget
from .datepicker import DateWidget


class MainPage:
    flights_xpath = "//a[@aria-controls='wizard-flight-pwa']"
    roundtrip_xpath = "//a[@aria-controls='wizard-flight-tab-roundtrip']"

    def __init__(self, browser: webdriver):
        self.browser = browser
        self.origin = LocationWidget(browser, "location-field-leg1-origin")
        self.destination = LocationWidget(browser, "location-field-leg1-destination")
        self.date_picker = DateWidget(browser, "d1", "d2")
        self.search_button_xpath = "//button[@data-testid='submit-button']"

    def select_flights(self):
        self.browser.find_element_by_xpath(MainPage.flights_xpath).click()

    def select_roundtrip(self):
        self.browser.find_element_by_xpath(MainPage.roundtrip_xpath).click()

    def pick_dates(self, start_date: datetime, end_date):
        self.date_picker.pick_date_range(start_date, end_date)

    def search(self):
        self.browser.find_element_by_xpath(self.search_button_xpath).click()
