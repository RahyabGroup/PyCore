import requests
from behave import *

from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.api_1_0.security_service_calls import test_user
from pystatic.test.test_behave.api_1_0.file import test_file_reused_steps


# url = 'http://localhost:8083/api/v1.0/prs'
#  files = {'file': open('/home/hoomanfr/Pictures/Wallpapers/python.jpg', 'rb')}
#  result = requests.post(url, files=files)


@When('we download the image file - file_download')
def step_impl(context):
    result = requests.get(Url.DOMAIN_ADDRESS + context.image_path)
    print(result)
    context.result = result


# @When('we upload an "{image_name}" file - image_upload')
# def step_impl(context, image_name):
#     headers = {"token": context.token}
#     # image_dict = {"file_name": "test_file_name"}
#     image_file = {'file_name.jpg': getattr(Constants, image_name, None)}
#     result = requests.post(Url.DOMAIN_ADDRESS + Url.IMAGE_UPLOAD_ROUTE.format("test_storage_name"), files=image_file, headers=headers)
#     print(result)
#     context.result = result


@then("the file will be downloaded successfully")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    # content_json = result.json()
    # message = content_json["message"]