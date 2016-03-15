Feature: as a  user I want to register to system

  Scenario: as a user I want to register to system
    Given Security is working
    When we register with our user_name and password - register
    Then the system will give a token after register

#
#  Scenario Outline: user can't register with <invalid_password>
#    Given IPN is working
#    When we register with our user_name and an "<invalid_password>" - register
#    Then the system wont give a token after register
#
#    Examples:
#      | invalid_password |
#      | wrongp           |
#      | None             |
#
#
#  Scenario: user can't register with an already registered user_name
#    Given IPN is working
#    When we register with our user_name and password - register
#    When we register again with the same user_name and a password - register
#    Then the system wont give a token after register
