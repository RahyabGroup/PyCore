from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we request getting that resource')
def step_impl(context):
    headers = {"token": context.token}
    result = requests.get(Url.DOMAIN_ADDRESS + "/resources/{}".format(context.resourceId), headers=headers)
    context.result = result
    print(result)


@then('the resource will be returned successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
