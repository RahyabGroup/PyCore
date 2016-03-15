Feature: remove a resource

  Scenario: remove a resource
    Given we are registered and logged in
    Given we added a resource
    When we remove that resource
    Then the resource will be removed successfully


