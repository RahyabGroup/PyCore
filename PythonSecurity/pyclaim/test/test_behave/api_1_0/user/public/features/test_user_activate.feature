# Created by root at 10/23/16
Feature: sysadmin can activate a  user

  Scenario: sysadmin can activate a registered user
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given sysadmin deactivated the user - user_deactivate
    When sysadmin activate the user - user_activate
    Then user will be activated successfully
