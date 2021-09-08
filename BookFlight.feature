Feature: Book a flight on Orbitz

  Scenario: Book most expensive roundtrip flight SFO-NY

    Given Navigate to Orbitz
    And Select Flights
    And Select Roundtrip
    And Leave from San Francisco
    And Fly to New York
    And Depart 2 weeks from today and return 3 weeks from today
    And Search
    Then Something

#    And Assert that the search result are rendered correctly
#    And Filter by Nonstop for destination flight
#    And Click on "Sort by" button
#    And pick "Price(Highest) from drop down menu
#    And click on the first flight on the top
#    And Filter by Nonstop for return
#    And Click on "Sort by" button
#    And pick "Price(Highest) from drop down menu
#    And click on the first flight on the top
#    And click on continue button
#    And click on "No, thanks" field in pop-up AD
#    When Click on check-out
#    Then Assert the flight details and price
