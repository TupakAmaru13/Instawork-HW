from selenium import webdriver


class FlightDetailsWidget:

    from_to_xpath = ".//div[@data-test-id='flight-review-header']/h2"
    airline_date_xpath = ".//div[@data-test-id='flight-review-header']//div[@data-test-id='flight-operated']"
    times_xpath = ".//div[@data-test-id='flight-summary']/h3/span"

    def __init__(self, browser: webdriver, parent_div_xpath):
        self.browser = browser
        self.parent_div_xpath = parent_div_xpath

    def get_flight_info(self):
        parent_div = self.browser.find_element_by_xpath(self.parent_div_xpath)
        return FlightInfo(
            parent_div.find_element_by_xpath(FlightDetailsWidget.from_to_xpath).text,
            parent_div.find_element_by_xpath(FlightDetailsWidget.airline_date_xpath).text,
            parent_div.find_element_by_xpath(FlightDetailsWidget.times_xpath).text
        )


class FlightInfo:

    def __init__(self, from_to: str, airline_date: str, times: str):
        self.from_to = from_to
        self.airline_date = airline_date
        self.times = times

    def __eq__(self, other):
        print(f"Comparing {self} and {other}")
        if isinstance(other, FlightInfo):
            return self.from_to == other.from_to and \
                self.airline_date == other.airline_date and \
                self.times == other.times
        return False

    def __repr__(self):
        return f"FlightInfo({self.from_to}, {self.airline_date}, {self.times})"