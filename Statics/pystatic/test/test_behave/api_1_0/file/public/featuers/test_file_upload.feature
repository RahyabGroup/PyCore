# Created by root at 10/13/15
Feature: as a user I can upload an image file to server

  Scenario: as a registered user we can upload an image to server
#    Given statics is up
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload a file - file_upload
    Then the file will be uploaded successfully


  Scenario Outline: as a registered user we can upload a valid image to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload an "<image_file>" file as "<image_name>"."<image_extension>" - file_upload
    Then the file will be uploaded successfully
    Examples:
    | image_file               | image_name   | image_extension  |
    | IMAGE_FILE_BINARY_PNG    | picture1     | PNG              |
    | IMAGE_FILE_BINARY_png    | picture2     | png              |
    | IMAGE_FILE_BINARY_PNG    | picture1     | PnG              |
    | IMAGE_FILE_BINARY_GIF    | picture3     | GIF              |
    | IMAGE_FILE_BINARY_gif    | picture4     | gif              |
    | IMAGE_FILE_BINARY_JPG    | picture5     | JPG              |
    | IMAGE_FILE_BINARY_jpg    | picture6     | jpg              |
    | IMAGE_FILE_BINARY_JPEG   | picture7     | JPEG             |
    | IMAGE_FILE_BINARY_jpeg   | picture8     | jpeg             |
#    | IMAGE_FILE_BINARY_jpeg   | عکس ۹        | jpeg             |


  Scenario Outline: as a registered user we can upload an duplicate image to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload an "<image_file>" file as "<image_name>"."<image_extension>" - file_upload
    Then the file will be uploaded successfully
    Examples:
    | image_file               | image_name   | image_extension  |
    | IMAGE_FILE_BINARY_PNG    | picture1     | PNG              |
    | IMAGE_FILE_BINARY_PNG    | picture1     | PNG              |


  Scenario: as a registered user we cant upload an empty image name to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload a file with empty file name - file_upload
    Then the file wont be uploaded


  Scenario: as a registered user we cant upload an image with empty extension to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload a file with empty extension - file_upload
    Then the file wont be uploaded


  Scenario: as a registered user we cant upload with an empty storage name to server
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    When we upload to an empty storage name - file_upload
    Then the empty file wont be uploaded


  Scenario: a not authenticated user cant upload an image
    Given we are logged in as sysadmin - login
    Given sysadmin registered a user with a user_name and password - user_create
    Given we are logged in with the user_name and password - login
    Given we are logged out of the system - logout
    When we upload a file - file_upload
    Then the file wont be uploaded for not authenticated user


  Scenario: sysadmin can upload an image to server
    Given we are logged in as sysadmin - login
    When we upload a file as sysadmin - file_upload
    Then the file will be uploaded successfully

#  Scenario: a deactivated user can upload an image
#    Given we are logged in as sysadmin - login
#    Given sysadmin registered a user with a user_name and password - user_create
#    Given sysadmin deactivated the user - user_deactivate
#    Given we are logged in with the user_name and password - login
#    When we upload a file - file_upload
#    Then the file will be uploaded successfully


#
#  Scenario Outline: as a registered user we cant upload an invalid image to server
#    Given we are logged in as sysadmin - login
#    Given sysadmin registered a user with a user_name and password - user_create
#    Given we are logged in with the user_name and password - login
#    When we upload an "<image_file>" file as "<image_name>"."<image_extension>" - file_upload
#    Then the file wont be uploaded
#    Examples:
#    | image_file               | image_name   | image_extension  |
#    | IMAGE_FILE_BINARY_BMP    | picture1     | BMP              |
#    | IMAGE_FILE_BINARY_bmp    | picture2     | bmp              |
#    | TEXT_FILE_BINARY_txt     | picture3     | txt              |
#    | IMAGE_FILE_EMPTY         | picture8     | jpeg             |

#  todo: farsi storage name

## todo : Scenario: big size images