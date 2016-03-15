# Created by root at 10/13/15
Feature: as a user I can download an image file from server

  Scenario: as a registered user we can download an image from server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we download the image file - file_download
    Then the file will be downloaded successfully

