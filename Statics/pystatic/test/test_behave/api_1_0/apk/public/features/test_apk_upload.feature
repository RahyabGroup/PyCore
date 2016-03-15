## Created by root at 10/13/15
Feature: as a user I can upload an apk file to server

  Scenario: as a registered user we can upload an apk file to server
#    Given statics is up
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file - apk_upload
    Then the apk file will be uploaded successfully


  Scenario Outline: sysadmin can upload a valid apk to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an "<apk_file>" file as "<apk_name>"."<apk_extension>" - apk_upload
    Then the apk file will be uploaded successfully
    Examples:
    | apk_file               | apk_name         | apk_extension  |
    | APK_FILE_BINARY_apk    | android_app1     | apk            |
    | APK_FILE_BINARY_APK    | android_app2     | APK            |
#    | APK_FILE_BINARY_APK    | فایل اپک     | APK            |


  Scenario Outline: sysadmin user we cant upload an invalid apk to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an "<apk_file>" file as "<apk_name>"."<apk_extension>" - apk_upload
    Then the apk file wont be uploaded
    Examples:
    | apk_file               | apk_name       | apk_extension  |
    | IMAGE_FILE_BINARY_BMP  | picture1       | BMP            |
    | IMAGE_FILE_BINARY_bmp  | picture2       | bmp            |
    | TEXT_FILE_BINARY_txt   | picture3       | txt            |
    | APK_FILE_EMPTY         | android_app2   | APK            |


  Scenario: sysadmin cant upload an apk file with duplicate name in the same package with different versions
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file - apk_upload
    And sysadmin uploads an apk file with same name and same package in the same storage _ apk_upload
    Then the apk file wont be uploaded


  Scenario: sysadmin cant upload an apk file with same filename and same version id and same package
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file - apk_upload
    And sysadmin uploads the same apk file again _ apk_upload
    Then the apk file wont be uploaded


  Scenario: as a registered user we cant upload an empty file name to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file with empty file name - apk_upload
    Then the apk file wont be uploaded


  Scenario: as a registered user we cant upload with an empty storage name to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file to an empty storage name - apk_upload
    Then the apk file wont be uploaded with empty storage name


  Scenario: as a registered user we cant upload with an empty package name to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file with an empty package name - apk_upload
    Then the apk file wont be uploaded


  Scenario: as a registered user we cant upload with an empty version id to server
    Given we are logged in as sysadmin - login
    When sysadmin uploads an apk file with an empty version id - apk_upload
    Then the apk file wont be uploaded


  Scenario: a not authenticated sysadmin cant upload an apk
    Given we are logged in as sysadmin - login
    Given we logged out of the system as sysadmin - logout
    When sysadmin uploads an apk file - apk_upload
    Then the apk file wont be uploaded for not authenticated user


  Scenario: a registered user other than sysadmin cant upload an apk
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload an apk file - apk_upload
    Then the apk file wont be uploaded for not authorized user

#
## todo : Scenario: big size apks
## todo: farsi storage name
## todo: farsi package name