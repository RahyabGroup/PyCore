Feature: get all resources

  Scenario: get all resources
    Given we are registered and logged in
    When we request to get all resources
    Then all resources will be returned to us successfully


