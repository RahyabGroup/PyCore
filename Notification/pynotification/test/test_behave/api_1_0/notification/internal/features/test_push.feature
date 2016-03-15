# Created by root at 1/4/16
Feature: a module can send a push request to notification server

  Scenario Outline: another IPN can send a push request to notification server
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an email and password - user_create
    When we send a push notification to the user "<userX>" with type "<message_type>" - push
    Then the request will be send successfully
    Examples:
    | userX | message_type  |
    | X     | wall-post     |