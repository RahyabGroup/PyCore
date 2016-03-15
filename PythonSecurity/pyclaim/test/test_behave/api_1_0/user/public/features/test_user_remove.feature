Feature: remove a user


  Scenario: sysadmin can remove a registered user
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When sysadmin removes the user account - user_remove
#    And sysadmin requests to see all users - user_get_all
    Then the account will be removed successfully