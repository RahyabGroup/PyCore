Feature: as a registered user we can get a user info by its id


  Scenario Outline: a registered user can get his user info by id
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an user_name and password - user_create
    Given user "<userX>" is logged in - login
    When user "<userX>" requests his user info by its id - user_get_by_id
    Then the user info will return successfully
    Examples:
      | userX  |
      | X      |


  Scenario Outline: a registered user cant get another users info by id
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<userX>" with an user_name and password - user_create
    Given sysadmin registered user "<userY>" with an user_name and password - user_create
    Given user "<userX>" is logged in - login
    When user "<userX>" requests the user "<userY>" info by its id - user_get_by_id
    Then the user info wont return
    Examples:
      | userX  | userY |
      | X      | Y     |


  Scenario Outline: sysadmin can get his user info by its id
    Given we are logged in as sysadmin - login
    When user "<sysadmin>" requests the user "<sysadmin>" info by its id - user_get_by_id
    Then the user info will return successfully
    Examples:
      | sysadmin  |
      | sysadmin  |


  Scenario: sysadmin can get another user info by its id
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When sysadmin requests the user by its id - user_get_by_id
    Then the user info will return successfully


  Scenario: sysadmin cant get his user info by invalid token
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged out of the system as sysadmin - logout
    When sysadmin requests the user by its id - user_get_by_id
    Then the user info wont return to not authenticated user


#  todo: remove user : invalid user id

