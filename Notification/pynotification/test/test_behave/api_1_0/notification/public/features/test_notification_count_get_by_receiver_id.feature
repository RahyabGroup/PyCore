# Created by root at 1/5/16
Feature: gives the count of notification of a user with a message type

  Scenario Outline: a registered user can get count of his notifications with a message type
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications count of user "<userX>" with type "<message_type>" - notification_count_get_by_receiver_id
    Then the list of notifications count will return successfully
  Examples:
    | userX | message_type  |
    | X     | wall-post     |


  Scenario Outline: a not authenticated can get his notification count
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    Given user "<userX>" is logged in - login
    Given user "<userX>" logged out from the system - logout
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications count of user "<userX>" with type "<message_type>" - notification_count_get_by_receiver_id
    Then the list of notifications count wont return to not authenticated user
    Examples:
      | userX | message_type  |
      | X     | wall-post     |


  Scenario Outline: a registered user cant get his notification count with empty message_type
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notifications count of user "<userX>" with empty message type - notification_count_get_by_receiver_id
    Then the list of notifications count wont return
    Examples:
      | userX | message_type  |
      | X     | wall-post     |