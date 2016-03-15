Feature: get all claim_types

  Scenario: get all claim_types
    Given we are registered and logged in
    When we request to get all claim_types
    Then all claim_types will be returned to us successfully


