from behave import step, then
from datetime import datetime, timedelta
from pages.mainpage import MainPage
from pages.flightsresult import FlightsResultsPage
from pages.orderconfirmation import ConfirmationPage


@step("Navigate to Orbitz")
def navigate_to_orbitz(context):
    context.browser.get("https://orbitz.com")
    context.window_handle = context.browser.current_window_handle


@step("Select Flights")
def select_flights(context):
    MainPage(context.browser).select_flights()


@step("Select Roundtrip")
def select_roundtrip(context):
    MainPage(context.browser).select_roundtrip()


@step("Leave from {origin}")
def leave_from(context, origin: str):
    MainPage(context.browser).origin.type_destination_and_select_first(origin)
    context.origin = origin


@step("Fly to {destination}")
def fly_to(context, destination: str):
    MainPage(context.browser).destination.type_destination_and_select_first(destination)
    context.destination = destination


@step("Depart {start_days_from_today} days from today and return {end_days_from_today} days from today")
def fly_on_date_range(context, start_days_from_today, end_days_from_today):
    today = datetime.today()
    context.start_date = today + timedelta(days=int(start_days_from_today))
    context.end_date = today + timedelta(days=int(end_days_from_today))
    MainPage(context.browser).date_picker.pick_date_range(context.start_date, context.end_date)


@step("Search")
def search(context):
    MainPage(context.browser).search()
    FlightsResultsPage(context.browser).wait_for_results()


@step("Assert results are for the correct parameters")
def assert_search_page_is_for(context):
    result_page = FlightsResultsPage(context.browser)
    assert context.origin in result_page.get_origin()
    assert context.destination in result_page.get_destination()
    start_date = context.start_date.strftime("%Y-%m-%d")
    print(start_date)
    print(result_page.get_departure_date())
    end_date = context.end_date.strftime("%Y-%m-%d")
    print(end_date)
    print(result_page.get_return_date())
    assert start_date == result_page.get_departure_date()
    assert end_date == result_page.get_return_date()


@step("Select nonstop flights")
def select_nonstop_flights(context):
    FlightsResultsPage(context.browser).select_nonstop()


@step("Sort flights by price descending")
def sort_flights_by_price_desc(context):
    FlightsResultsPage(context.browser).sort_results_by_price_desc()


@step("Select first flight")
def select_first_flight(context):
    FlightsResultsPage(context.browser).select_first_flight()


@step("Confirm departure flight")
def confirm_departure_flight(context):
    page = FlightsResultsPage(context.browser)
    flight_info = page.get_selected_flight_info()
    context.departure_flight_info = flight_info
    page.confirm_flight_selection()
    page.wait_for_results()


@step("Confirm return flight")
def confirm_return_flight(context):
    page = FlightsResultsPage(context.browser)
    flight_info = page.get_selected_flight_info()
    context.return_flight_info = flight_info
    context.price = page.get_expected_price()
    page.confirm_flight_selection()
    # new tab was opened, switch to it
    context.browser.switch_to_window(context.browser.window_handles[1])


@then("Assert flight details")
def assert_flight_details(context):
    page = ConfirmationPage(context.browser)
    page.wait_for_load()
    assert context.departure_flight_info == page.get_departure_flight_info()
    assert context.return_flight_info == page.get_return_flight_info()
    assert context.price == page.get_price()
