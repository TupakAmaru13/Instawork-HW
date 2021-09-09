from selenium import webdriver


class LocationWidget:

    def __init__(self, browser: webdriver, base_name: str):
        self.base_name = base_name
        self.browser = browser
        self.button_xpath = f'//button[@data-stid="{base_name}-menu-trigger"]'
        self.closed_input_xpath = f'//input[@data-stid="{base_name}-input"]'
        self.input_xpath = f'//input[@data-stid="{base_name}-menu-input"]'
        self.first_result_xpath = f'//ul[@data-stid="{base_name}-results"]/li[1]/button'

    def type_destination_and_select_first(self, destination: str):
        self.browser.find_element_by_xpath(self.button_xpath).click()
        self.browser.find_element_by_xpath(self.input_xpath).send_keys(destination)
        self.browser.find_element_by_xpath(self.first_result_xpath).click()

    def get_value(self) -> str:
        return self.browser.find_element_by_xpath(self.closed_input_xpath).get_attribute('value')
