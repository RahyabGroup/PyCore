Feature: remove a claim of a resource

  Scenario: remove a claim of a resource
    Given we are registered and logged in
    Given we added a resource
    Given we have a claim_type
    Given we have a claim with that claim_type in resource
    When we remove that claim of the resource
    Then the claim will be removed successfully


