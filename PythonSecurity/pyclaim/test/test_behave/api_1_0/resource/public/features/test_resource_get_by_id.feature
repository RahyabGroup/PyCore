Feature: get a resource by its Id

  Scenario: get a resource by its Id
    Given we are registered and logged in
    Given we added a resource
    When we request getting that resource
    Then the resource will be returned successfully


