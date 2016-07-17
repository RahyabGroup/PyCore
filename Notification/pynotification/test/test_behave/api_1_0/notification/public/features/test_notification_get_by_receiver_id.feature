# Created by root at 1/5/16
Feature: a user can get list of his notifications
  # Enter feature description here

  Scenario Outline: a registered user get his notifications with user and message id
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    Then the list of notifications will return successfully
  Examples:
    | userX | message_type  |
    | X     | wall-post     |


  Scenario Outline: a not authenticated user can get his notifications
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given user "<userX>" logged out from the system - logout
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    Then the list of notifications wont return to not authenticated user
    Examples:
      | userX | message_type  |
      | X     | wall-post     |


  Scenario Outline: a registered user cant get his notifications with empty message_type
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications of user "<userX>" with empty message_type - notification_get_by_receiver_id
    Then the list of notifications wont return
    Examples:
      | userX | message_type  |
      | X     | wall-post     |


  Scenario Outline: a registered user cant get his notifications with empty query_string
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications of user "<userX>" with type "<message_type>" and empty query string - notification_get_by_receiver_id
    Then the list of notifications wont return
    Examples:
      | userX | message_type  |
      | X     | wall-post     |