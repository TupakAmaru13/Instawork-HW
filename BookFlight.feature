Feature: Book a flight on Orbitz

  Scenario: Book most expensive roundtrip flight SFO-NY

    Given Navigate to Orbitz
    When Select Flights
    And Select Roundtrip
    And Leave from San Francisco
    And Fly to New York
    And Depart 14 days from today and return 21 days from today
    And Search
    And Assert results are for the correct parameters
    And Select nonstop flights
    And Sort flights by price descending
    And Select first flight
    And Confirm departure flight
    And Select nonstop flights
    And Sort flights by price descending
    And Select first flight
    And Confirm return flight
    Then Assert flight details
