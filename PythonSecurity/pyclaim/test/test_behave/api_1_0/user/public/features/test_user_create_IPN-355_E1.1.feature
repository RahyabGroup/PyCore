#  Feature: کاربر خارجی باید بتواند در سیستم ثبت نام کند
Feature: register a user

  Scenario: sysadmin can register a new user
    Given we are logged in as sysadmin - login
    When sysadmin create a user with an user_name and password - user_create
    Then the user will be created successfully

  Scenario: register user with duplicate user_name
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When sysadmin register a user with an already exist user_name - user_create
    Then the user wont be registered


  Scenario: register user with an invalid password
    Given we are logged in as sysadmin - login
    When sysadmin register a user with an invalid password - user_create
    Then the user wont be registered

  Scenario: user can't register with None password
    Given we are logged in as sysadmin - login
    When sysadmin register a user with an user_name and a None password - user_create
    Then the user wont be registered

  Scenario: user who is registered can't login with None user_name
    Given we are logged in as sysadmin - login
    When sysadmin register a user with None as user_name and a password - user_create
    Then the user wont be registered

#  Scenario: register user with a deleted user_name
#     Given X is a deleted account
#      When sysadmin register a user with user_name of X
#      Then the user X will be registered successfully

#    Scenario: register user with an invalid user_name
#    Given we are logged in as sysadmin - login
#    When sysadmin register a user with an invalid user_name - user_create
#    Then the user wont be registered
