from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we request to get all resources')
def step_impl(context):
    headers = {"token": context.token}
    result = requests.get(Url.DOMAIN_ADDRESS + "/resources", headers=headers)
    context.result = result
    print(result)


@then('all resources will be returned to us successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
