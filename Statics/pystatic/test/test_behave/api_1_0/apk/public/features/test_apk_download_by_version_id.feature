# Created by root at 10/13/15
Feature: as a user I can download an apk by version id from server

  Scenario: as a registered user we can download the apk from server
    Given we are logged in as sysadmin - login
    Given sysadmin uploaded an apk file - apk_upload
    When we download the apk file by version id - apk_download
    Then the apk file will be downloaded successfully

