from behave import *
import requests

from pystatic.test.test_behave.resources.constants import Constants
from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader


@Given('we uploaded an image file - file_upload')
def step_impl(context):
    headers = {"token": context.token}
    image_file = {'file_name.jpg': Constants.IMAGE_FILE_BINARY_gif}
    context.storage_name = "test_storage_name"
    result = requests.post(Url.DOMAIN_ADDRESS + Url.FILE_UPLOAD_ROUTE.format(context.storage_name), files=image_file, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = ResponseReader.get_body(result)
    context.image_path = message["path"]
    context.image_name = message["file_name"]


