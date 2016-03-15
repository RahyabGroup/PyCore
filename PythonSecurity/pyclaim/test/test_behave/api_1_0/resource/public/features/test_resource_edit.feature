Feature: edit a resource

  Scenario: edit a resource
    Given we are registered and logged in
    Given we added a resource
    When we edit that resource
    Then the resource will be edited successfully


