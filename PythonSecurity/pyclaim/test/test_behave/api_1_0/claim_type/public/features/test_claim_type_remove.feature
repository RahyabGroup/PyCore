Feature: remove a claim_type

  Scenario: remove a claim_type
    Given we are registered and logged in
    Given we added a claim_type
    When we remove that claim_type
    Then the claim_type will be removed successfully


