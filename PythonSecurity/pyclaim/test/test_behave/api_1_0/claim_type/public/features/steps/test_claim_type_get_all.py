from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we request to get all claim_types')
def step_create_a_claim_type(context):
    headers = {"token": context.token}
    result = requests.get(Url.DOMAIN_ADDRESS + "/claimtypes", headers=headers)
    context.result = result
    print(result)


@then('all claim_types will be returned to us successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
