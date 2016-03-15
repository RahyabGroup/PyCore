# Created by root at 10/13/15
Feature: as a user I can upload an image file to server

  Scenario: as a registered user we can replace an image to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file - file_replace
    And we download the image file - file_download
    Then the file will be replaced successfully


  Scenario: as a registered user we cant replace an image to server with empty storage name
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with empty storage_name - file_replace
    Then the file wont be replaced


  Scenario: as a registered user we cant replace an image to server with empty old file name
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with empty old_file_name - file_replace
    Then the file wont be replaced

  Scenario: as a registered user we cant replace an image to server with invalid old file extention
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with invalid old_file_extention - file_replace
    Then the file wont be replaced


  Scenario: as a registered user we cant replace an image to server with empty new file name
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with empty new_file_name - file_replace
    Then the file wont be replaced


  Scenario: as a registered user we cant replace an image to server with empty new file content
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with empty new_file_content - file_replace
    Then the file wont be replaced

  Scenario: as a registered user we cant replace an image to server with empty new file extention
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we uploaded an image file - file_upload
    When we replace the file with empty new_file_extention - file_replace
    Then the file wont be replaced