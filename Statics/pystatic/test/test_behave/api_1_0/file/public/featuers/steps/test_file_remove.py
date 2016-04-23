from behave import *
import requests
from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader


@when("we remove the image file - file_remove")
def step_impl(context):
    headers = {"token": context.token}
    # image_info = {'storage_name': context.storage_name, "path": context.image_path}
    url = Url.DOMAIN_ADDRESS + Url.FILE_REMOVE_ROUTE.format(context.storage_name, context.image_name)
    result = requests.delete(url, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@then("the file does not exist")
def step_impl(context):
    result = context.result
    result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
