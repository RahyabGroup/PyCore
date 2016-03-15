from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we remove that claim of the resource')
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + "/resources/{}/claims/{}".format(context.resourceId, context.claimId), headers=headers)
    context.result = result
    print(result)


@then('the claim will be removed successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
