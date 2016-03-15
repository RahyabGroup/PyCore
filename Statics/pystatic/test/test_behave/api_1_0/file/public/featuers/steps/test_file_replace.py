from behave import *
from pyutil.file import file_info
import requests

from pystatic.test.test_behave.resources.constants import Constants
from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader

use_step_matcher("re")


@when("we replace the file - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_BMP}
    result = requests.put(Url.DOMAIN_ADDRESS + context.image_path, files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@then("the file will be replaced successfully")
def step_impl(context):
    replace_result = context.replace_result
    assert replace_result.status_code == ResponseStatusCodes.PUT_SUCCESS
    get_result = context.result
    assert get_result.status_code == ResponseStatusCodes.GET_SUCCESS
    content = get_result.content
    assert content == Constants.IMAGE_FILE_BINARY_BMP
    assert content != Constants.IMAGE_FILE_BINARY_gif
    print(content)


@when("we replace the file with empty storage_name - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_BMP}
    old_file_name = context.image_name
    result = requests.put("{}/files/ /{}".format(Url.DOMAIN_ADDRESS, old_file_name), files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@then("the file wont be replaced")
def step_impl(context):
    replace_result = context.replace_result
    assert replace_result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    message = ResponseReader.get_body(replace_result)
    print(message)


@when("we replace the file with empty old_file_name - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_BMP}
    result = requests.put("{}/files/{}/ ".format(Url.DOMAIN_ADDRESS, context.storage_name), files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@when("we replace the file with invalid old_file_extention - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_BMP}
    old_file_name_without_extention = file_info.get_file_name(context.image_name)
    result = requests.put("{}/files/{}/{}".format(Url.DOMAIN_ADDRESS, context.storage_name, old_file_name_without_extention), files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@when("we replace the file with empty new_file_name - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {' ': Constants.IMAGE_FILE_BINARY_BMP}
    result = requests.put(Url.DOMAIN_ADDRESS + context.image_path, files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@when("we replace the file with empty new_file_content - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': ""}
    result = requests.put(Url.DOMAIN_ADDRESS + context.image_path, files=image_file, headers=headers)
    print(result)
    context.replace_result = result


@when("we replace the file with empty new_file_extention - file_replace")
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name': Constants.IMAGE_FILE_BINARY_BMP}
    result = requests.put(Url.DOMAIN_ADDRESS + context.image_path, files=image_file, headers=headers)
    print(result)
    context.replace_result = result