# Created by root at 10/23/16
Feature: sysadmin can deactivate a  user

  Scenario: sysadmin can deactivate a registered user
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When sysadmin deactivate the user - user_deactivate
    Then user will be deactivated successfully
