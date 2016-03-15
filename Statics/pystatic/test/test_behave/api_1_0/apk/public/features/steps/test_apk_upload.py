from bson.objectid import ObjectId
import requests
from behave import *

from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.resources.constants import Constants



# url = 'http://localhost:8083/api/v1.0/prs'
#  files = {'file': open('/home/hoomanfr/Pictures/Wallpapers/python.jpg', 'rb')}
#  result = requests.post(url, files=files)

from pystatic.test.test_behave.test_utilities import utility
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader


@When('sysadmin uploads an apk file - apk_upload')
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'file_name.apk': Constants.APK_FILE_BINARY_apk}
    context.apk_file_name = 'file_name.apk'
    version_id = utility.generate_simple_unique_int()
    context.version_id = version_id
    storage_name = "android_test"
    context.storage_name = storage_name
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    context.package_name = apk_dict["package_name"]
    context.version = apk_dict["version"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@then("the apk file will be uploaded successfully")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS


@When('sysadmin uploads an "{apk_file}" file as "{apk_name}"."{apk_extension}" - apk_upload')
def step_impl(context, apk_file, apk_name, apk_extension):
    headers = {"token": context.users["sysadmin"]["token"]}
    version_id = utility.generate_simple_unique_int()
    context.version_id = version_id
    storage_name = "android_test"
    context.storage_name = storage_name
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    apk_file_dict = {"{}.{}".format(u"{}".format(apk_name), apk_extension): getattr(Constants, apk_file, None)}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file_dict, headers=headers)
    print(result)
    context.result = result


@step("sysadmin uploads the same apk file again _ apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_dict = {"package_name": context.package_name, "version": context.version, "version_id": context.version_id}
    apk_file = {"{}".format(context.apk_file_name): Constants.APK_FILE_BINARY_apk}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(context.storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@step("sysadmin uploads an apk file with same name and same package in the same storage _ apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_dict = {"package_name": context.package_name, "version": context.version, "version_id": utility.generate_simple_unique_int()}
    apk_file = {"{}".format(context.apk_file_name): Constants.APK_FILE_BINARY_apk}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(context.storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@when("sysadmin uploads an apk file with empty file name - apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'.apk': Constants.APK_FILE_BINARY_apk}
    version_id = utility.generate_simple_unique_int()
    storage_name = "android_test"
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@when("sysadmin uploads an apk file to an empty storage name - apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'apk_file_name.apk': Constants.APK_FILE_BINARY_apk}
    version_id = utility.generate_simple_unique_int()
    storage_name = ""
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@when("sysadmin uploads an apk file with an empty package name - apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'apk_file_name.apk': Constants.APK_FILE_BINARY_apk}
    version_id = utility.generate_simple_unique_int()
    storage_name = "android_test"
    apk_dict = {"package_name": "", "version": "1.0.0", "version_id": version_id}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@when("sysadmin uploads an apk file with an empty version id - apk_upload")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'apk_file_name.apk': Constants.APK_FILE_BINARY_apk}
    # version_id = utility.generate_simple_unique_int()
    storage_name = "android_test"
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": 0}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@When('we upload an apk file - apk_upload')
def step_impl(context):
    headers = {"token": context.token}
    apk_file = {'file_name.apk': Constants.APK_FILE_BINARY_apk}
    version_id = utility.generate_simple_unique_int()
    storage_name = "android_test"
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    context.version = apk_dict["version"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    context.result = result


@then("the apk file wont be uploaded")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR


@then("the apk file wont be uploaded for not authorized user")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHORIZED_ERROR


@then("the apk file wont be uploaded for not authenticated user")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR


@then("the apk file wont be uploaded with empty storage name")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.PAGE_NOT_FOUND_ERROR


# @When('sysadmin uploads a duplicate "{apk_file}" file as "{apk_name}"."{apk_extension}" with "{apk_package}" - apk_upload')
# def step_impl(context, apk_file, apk_name, apk_extension, apk_package):
#     headers = {"token": context.users["sysadmin"]["token"]}
#     version_id = utility.generate_simple_unique_int()
#     context.version_id = version_id
#     storage_name = "android_test"
#     context.storage_name = storage_name
#     apk_dict = {"package_name": apk_package, "version": "1.0.0", "version_id": version_id}
#     apk_file = {"{}.{}".format(u"{}".format(apk_name), apk_extension): getattr(Constants, apk_file, None)}
#     result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
#     print(result)
#     context.result = result
