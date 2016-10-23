#  Feature:کاربر ثبت شده بايد بتواند با ارايه نام کاربري و رمز عبور وارد سيستم شود.
Feature: as a user I want to login to system

  Scenario: user who is registered can login
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When we login with the user_name and password - login
    Then the system will give us a token

  Scenario Outline: user who is registered can't login with <wrongpassword> password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When we login with the user_name and a "<wrongpassword>" password - login
    Then the system wont give us a token

    Examples:
      | wrongpassword |
      | wrongpas      |
      | None          |


  Scenario Outline: user who is registered can't login with <wronguser_name> user_name
    Given IPN is working
    When we login with a "<wronguser_name>" as user_name and a password - login
    Then the system wont give us a token

    Examples:
      | wronguser_name                  |
      | Unregistereduser_name@parsa.com |
      | None                        |



  Scenario: deactivated user cant login
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given sysadmin deactivated the user - user_deactivate
    When we login with the user_name and password - login
    Then the system wont give us a token

##    todo : user_name casesensitive
