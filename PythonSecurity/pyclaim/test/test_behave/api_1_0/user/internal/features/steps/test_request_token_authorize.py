from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url


@when('we check if the token is authorized')
def step_impl(context):
    result = requests.get(Url.DOMAIN_ADDRESS + "/internal/accounts/token_authorize/{}".format(context.token))
    context.result = result
    print(result)


@then('the system will confirm that token is authorized')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("\nmessage: ", message)
    assert result.status_code == client.OK
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
