#  Feature:کاربر ثبت شده بايد بتواند در صورت فراموشي رمز عبور آن را بازيابي کند.
Feature: as a user I want to restore my forgotten password so I can login into system

  Scenario: user who forgot his password can restore it
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When we tell the system that the password is forgotten for our user_name - password_remember
    Then the system will send us the password in clear text
    #the system will send an user_name with link to reset password

  Scenario: user who gives an invalid user_name can't restore a password
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with an user_name and password _ user_create
    When we tell the system that the password is forgotten with invalid user_name - password_remember
    Then the password wont send to us


#  Scenario: user who gives a None user_name can't restore a password
#    Given IPN is working
#    When we tell the system that the password is forgotten for an unregistered user_name
#    Then the system will give an error
