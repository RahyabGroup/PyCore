# Created by root at 10/13/15
Feature: as a user I can download an apk file from server

  Scenario: as a registered user we can download an image from server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given sysadmin uploaded an apk file - apk_upload
    When we download the apk file - apk_download
    Then the apk file will be downloaded successfully


