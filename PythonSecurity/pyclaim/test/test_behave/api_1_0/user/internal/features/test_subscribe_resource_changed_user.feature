Feature: subscribe_resource_changed_user

  Scenario: subscribe_resource_changed_user
    Given we are registered and logged in
    Given we added a resource
    When we subscribe_resource_changed_user
    Then the service will subscribe_resource_changed_user


