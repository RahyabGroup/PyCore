Feature: as a user I want to logout from system

  Scenario: as a registered user I want to logout from system
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged in with the user_name and password - login
    When we log out from the system - logout
    Then we will be logged out successfully


  Scenario: as a not authenticated user I cant logout from system
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged in with the user_name and password - login
    Given we logged out from the system - logout
    When we log out from the system with the same token - logout
    Then we will be logged out successfully
#
##    Scenario: as a not authenticated user I cant logout from system # can logout
##    Given we are logged in as sysadmin - login
##    Given sysadmin registered a user with an user_name and password _ user_create
##    # When we log out from the system with a not valid token
##    Then the system wont accept our request