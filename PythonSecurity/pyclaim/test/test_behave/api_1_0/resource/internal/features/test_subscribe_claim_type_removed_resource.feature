Feature: subscribe claim_type removed resource

  Scenario: subscribe claim_type removed resource
    Given we are registered and logged in
    Given we have a claim_type
    When we subscribe claim_type removed resource
    Then the claim_type will be removed successfully


