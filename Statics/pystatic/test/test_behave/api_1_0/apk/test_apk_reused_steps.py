from bson import ObjectId

from pystatic.test.test_behave.test_utilities import utility
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'root'

from pystatic.test.test_behave.resources.constants import Constants
from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from behave import *
import requests


@Given('sysadmin uploaded an apk file - apk_upload')
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    apk_file = {'file_name.apk': Constants.IMAGE_FILE_BINARY_gif}
    version_id = utility.generate_simple_unique_int()
    context.version_id = version_id
    storage_name = "android_test"
    context.storage_name = storage_name
    apk_dict = {"package_name": "com.parsa.{}".format(str(ObjectId())), "version": "1.0.0", "version_id": version_id}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.APK_UPLOAD_ROUTE.format(storage_name), params=apk_dict, files=apk_file, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = ResponseReader.get_body(result)
    context.apk_path = message
