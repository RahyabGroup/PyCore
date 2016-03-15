Feature: get all users


  Scenario: sysadmin can get all users info
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When sysadmin requests to see all users - user_get_all
    Then list of all users will return successfully


  Scenario Outline: a registered user cant get all users info
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an user_name and password - user_create
    Given user "<userX>" is logged in - login
    When user "<userX>" requests all users info - user_get_all
    Then the users info wont return to not authorized user
    Examples:
      | userX  |
      | X      |


  Scenario: sysadmin cant get all users info by invalid token
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged out of the system as sysadmin - logout
    When sysadmin requests to see all users - user_get_all
    Then the user info wont return to not authenticated user


#  todo: remove user : invalid user id

