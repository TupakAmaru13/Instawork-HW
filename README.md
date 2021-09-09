# Instawork take-home assignment
## Author
Tatiana Volk, [tatiana.volk@gmail.com](mailto:tatiana.volk@gmail.com)

## Requriements
(copied from the document sent to me)

Using selenium with any programming language and test framework of your choice, implement
the following:
- Visit www.orbitz.com website.
- Select Flights
- Select “Roundtrip”.
- Enter “Leaving from” : San Francisco and “Going to”: New York.
- Select “Departing” date to be 2 weeks from today and “Returning” date to be 3 weeks
from today.
- Click on Search.
- Assert that the search results are rendered correctly (Ex: Departure/Arrival location and
dates match the input data).
- Select “Nonstop” flights.
- Select the most expensive flight from the list.
- Click on “Select” and then click on “Select this fare” to book.
- Assert the flight details & price on the flight review page.

## Implementation

### Notes
Orbitz's interface seems to have changed since the assignment was created. Most
of the second half of the steps look and work differently now. I chose to implement the test in
accordance to the actual interface, following the spirit of the requirements rather than the letter.

There's some flakiness around selecting the flight dates, which probably needs further investigation.

### Set up
The test is implemented in Python, using `behave` and `selenium`. Before running the test, a `python` executable
is required (Python 3.9 was used during development), the necessary libraries should be installed by:
```shell
pip install -r requirements.txt
```

Also, the appropriate browser driver for Selenium should be downloaded. This test uses the Chrome driver,
which can be downloaded from the [driver download page](https://chromedriver.chromium.org/downloads). The archive
should be unpacked and the binary should be placed somewhere in the `$PATH`.

### Running the test
The test is launched using the `behave` runner:
```shell
behave -i BookFlight.feature
```
