Feature: edit a user's user_name and password

  Scenario: authenticated user cant edit his user_name and password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged in with the user_name and password - login
    When we edit our user_name and password - user_edit
    Then the user_name and password wont change for not authorized user


  Scenario: not authenticated user cant edit his user_name and password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    Given we logged in with the user_name and password - login
    Given we logged out from the system - logout
    When we edit our user_name and password - user_edit
    Then the user_name and password wont change


  Scenario Outline: sysadmin  cant change his user_name to an already exist user_name
    Given we are logged in as sysadmin - login
    Given sysadmin created user "<userX>" with an user_name and password - user_create
    When sysadmin changes his user_name to user "<userX>" user_name - user_edit
    Then the user_name wont change
    Examples:
      | userX |
      | X     |

  Scenario Outline: sysadmin can edit his user_name and password
    Given we are logged in as sysadmin - login
    When sysadmin edit his user_name to "<user_name>" and password to "<password>" - user_edit
    And sysadmin edit his user_name to "<olduser_name>" and password to "<oldpassword>" - user_edit
    Then the user_name and password will change successfully
    Examples:
      | user_name                    | password       | olduser_name              | oldpassword           |
      | editedsysadmin@gamil.com | editedpassword | sysadmin@security.com | sysadmin@security.com |
