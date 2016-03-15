Feature: create a claim for a resource

  Scenario: create a claim for a resource
    Given we are registered and logged in
    Given we added a resource
    Given we have a claim_type
    When we add a claim for that resource with the claim_type
    Then the claim will be added to resource successfully


