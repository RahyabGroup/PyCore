Feature: create a claim_type


  Scenario Outline: sysadmin can create a claim_type
    Given we are logged in as sysadmin - login
    When we create a claim_type as user "<sysadmin>" - claim_type_create
    Then the claim_type will be added successfully
    Examples:
    | sysadmin |
    | sysadmin |


  Scenario Outline: a registered user cant create a claim_type
    Given we are logged in as sysadmin - login
    Given sysadmin registered user "<UserX>" with an user_name and password - user_create
    Given user "<UserX>" is logged in - login
    When we create a claim_type as user "<UserX>" - claim_type_create
    Then the claim_type wont create for not authorized user
    Examples:
    | UserX |
    | UserX |


  Scenario Outline: sysadmin cant create a claim-type with duplicate name
    Given we are logged in as sysadmin - login
    When we create a claim_type as user "<sysadmin>" - claim_type_create
    When we create a claim_type with duplicate name as user "<sysadmin>" - claim_type_create
    Then the claim_type wont create
    Examples:
    |sysadmin |
    |sysadmin |


    Scenario Outline: sysadmin cant create a claim_type with empty name
    Given we are logged in as sysadmin - login
    When we create a claim_type with empty name as user "<sysadmin>" - claim_type_create
    Then the claim_type wont create
    Examples:
    |sysadmin |
    |sysadmin |

