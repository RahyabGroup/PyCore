Feature: check if subscribe user changed account
#
#  Scenario: check if subscribe user changed account
#    Given we are registered and logged in
#    When we check if the user_id is authorized
#    Then the system will confirm that user_id is authorized
#  =======
##  Feature:کاربر ثبت شده بايد بتواند با ارايه نام کاربري و رمز عبور وارد سيستم شود.
#Feature: as a user I want to login into system
#
#  Scenario: user who is registered can login
#    Given the user is registered
#    When we give our user_name and password
#    Then the system will give a token
#
#  Scenario Outline: user who is registered can't login with <wrongpassword> password
#    Given the user is registered
#    When we give our user_name and a "<wrongpassword>" password
#    Then the system wont give a token
#
#    Examples:
#      | wrongpassword |
#      | wrongpass     |
#      | None          |
#
##  Scenario: user who is registered can't login with None password
##     Given the user is registered
##      When we give our user_name and a None password
##      Then the system wont give a token
#
#  Scenario Outline: user who is registered can't login with <wronguser_name> user_name
#    Given IPN is working
#    When we give "<wronguser_name>" as user_name and a password
#    Then the system wont give a token
#
#    Examples:
#      | wronguser_name                  |
#      | Unregistereduser_name@parsa.com |
#      | None                        |
#
##  Scenario: user can't login with unregistered user_name
##     Given IPN is working
##      When we give our unregistered user_name and a password
##      Then the system wont give a token
