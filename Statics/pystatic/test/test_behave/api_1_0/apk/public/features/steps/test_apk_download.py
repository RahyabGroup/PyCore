import requests
from behave import *

from pystatic.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pystatic.test.test_behave.resources.url_addresses import Url
from pystatic.test.test_behave.api_1_0.apk import test_apk_reused_steps
from pystatic.test.test_behave.api_1_0.security_service_calls import test_user
from pystatic.test.test_behave.test_utilities.response_reader import ResponseReader


@When('we download the apk file - apk_download')
def step_impl(context):
    result = requests.get(Url.DOMAIN_ADDRESS + context.apk_path["apk_path"])
    print(result)
    context.result = result


@then("the apk file will be downloaded successfully")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    # message = ResonseReader.get_body(result)