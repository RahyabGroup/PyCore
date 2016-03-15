# Created by root at 12/16/15
Feature: a user can change his password

  Scenario: a registered user can change his password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we are logged in with the user_name and password - login
    When we change our password - password_change
    Then the password will be changed successfully


  Scenario: a registered user cant change his password with wrong old password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we are logged in with the user_name and password - login
    When we change our password with wrong old password - password_change
    Then the password wont be changed