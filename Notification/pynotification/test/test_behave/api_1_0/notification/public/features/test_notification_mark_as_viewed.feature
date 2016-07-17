# Created by root at 1/5/16
Feature: after viewing a notification by user, it's status should change to viewed

  Scenario Outline: a registered user can change a notification status to viewed
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notification of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    When we change the notification status to read as user "<userX>" _ notification_mark_as_viewed
    Then the notification status will change successfully
    Examples:
    | userX    | message_type   |
    | X        | new_message    |


  Scenario Outline: a registered user cant mark his notification as viewed with empty notification id
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notification of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    When we change the notification status to read as user "<userX>" with empty notification id _ notification_mark_as_viewed
    Then the notification status wont change
    Examples:
      | userX | message_type  |
      | X     | wall-post     |


  Scenario Outline: a registered user cant mark his notification as viewed with invalid notification id
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with a user_name and password - user_create
    Given user "<userX>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notification of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    When we change the notification status to read as user "<userX>" with invalid notification id _ notification_mark_as_viewed
    Then the notification status wont change
    Examples:
      | userX | message_type  |
      | X     | wall-post     |


  Scenario Outline: a registered user cant mark another persons notification as viewed
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    Given user "<userX>" is logged in - login
    Given sysadmin registered user "<userY>" with an email and password - user_create
    Given user "<userY>" is logged in - login
    Given we sent a push notification to the user "<userX>" with type "<message_type>" - push
    When we get the notification of user "<userX>" with type "<message_type>" - notification_get_by_receiver_id
    When we change the notification status to read as user "<userY>" _ notification_mark_as_viewed
    Then the notification status wont change
    Examples:
      | userX | userY | message_type  |
      | X     | Y     | wall-post     |