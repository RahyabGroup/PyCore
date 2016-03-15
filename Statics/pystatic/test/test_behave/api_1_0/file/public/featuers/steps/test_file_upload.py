import requests

from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.api_1_0.security_service_calls import test_user
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'H.Rouhani'

from behave import *
from pystatic.test.test_behave.resources.constants import Constants


# url = 'http://localhost:8083/api/v1.0/prs'
#  files = {'file': open('/home/hoomanfr/Pictures/Wallpapers/python.jpg', 'rb')}
#  result = requests.post(url, files=files)


@When('we upload a file - file_upload')
def step_impl(context):
    headers = {"token": context.token}
    # image_dict = {"file_name": "test_file_name"}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_gif}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
    print(result)
    context.result = result


@When('we upload an "{image_file}" file as "{image_name}"."{image_extension}" - file_upload')
def step_impl(context, image_file, image_name, image_extension):
    headers = {"token": context.token}
    # image_dict = {"file_name": "test_file_name"}
    image_file = {"{}.{}".format(u"{}".format(image_name), image_extension): getattr(Constants, image_file, None)}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
    print(result)
    context.result = result


@When('we upload a file with empty file name - file_upload')
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'.jpg': Constants.IMAGE_FILE_BINARY_gif}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
    print(result)
    context.result = result


@When('we upload a file with empty extension - file_upload')
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file.': Constants.IMAGE_FILE_BINARY_gif}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
    print(result)
    context.result = result


@When('we upload to an empty storage name - file_upload')
def step_impl(context):
    headers = {"token": context.token}
    # image_dict = {"file_name": "test_file_name"}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_gif}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format(""), files=image_file, headers=headers)
    print(result)
    context.result = result


@When('we upload a file as sysadmin - file_upload')
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_gif}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
    print(result)
    context.result = result


@given("statics is up")
def step_impl(context):
    pass


@then("the file will be uploaded successfully")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS


@then("the file wont be uploaded")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR


@then("the empty file wont be uploaded")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.PAGE_NOT_FOUND_ERROR


@then("the file wont be uploaded for not authenticated user")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR