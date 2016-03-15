from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('sysadmin requests to see all users - user_get_all')
def step_impl(context):
    headers = {"token": context.sysadmin_token}
    get_params = {"skip": 0, "take": 150}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.USER_GET_ALL_ROUTE, headers=headers, params=get_params)
    context.result = result
    print(result)


@when('user "{user_x}" requests all users info - user_get_all')
def step_impl(context, user_x):
    headers = {"token": context.users[user_x]["token"]}
    get_params = {"skip": 0, "take": 150}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.USER_GET_ALL_ROUTE, headers=headers, params=get_params)
    context.result = result
    print(result)


@then('list of all users will return successfully')
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    message = ResponseReader.get_body(result)
    if message:
        for row in message:
            print(row, "\n")


@then("the users info wont return to not authorized user")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.NOT_AUTHORIZED_ERROR


@then("the users info wont return to not authenticated user")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR