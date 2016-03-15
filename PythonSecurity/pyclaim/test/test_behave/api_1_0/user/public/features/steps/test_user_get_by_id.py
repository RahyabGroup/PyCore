from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('sysadmin requests the user by its id - user_get_by_id')
def step_impl(context):
    user_id = context.user_id
    headers = {"token": context.sysadmin_token}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.USER_GET_BY_ID_ROUTE.format(user_id), headers=headers)
    context.result = result
    print(result)


@when('user "{user_x}" requests the user "{user_y}" info by its id - user_get_by_id')
def step_impl(context, user_x, user_y):
    headers = {"token": context.users[user_x]["token"]}
    user_id = context.users[user_y]["id"]
    result = requests.get(Url.DOMAIN_ADDRESS + Url.USER_GET_BY_ID_ROUTE.format(user_id), headers=headers)
    context.result = result
    print(result)


@when('user "{user_x}" requests his user info by its id - user_get_by_id')
def step_impl(context, user_x):
    headers = {"token": context.users[user_x]["token"]}
    user_id = context.users[user_x]["id"]
    result = requests.get(Url.DOMAIN_ADDRESS + Url.USER_GET_BY_ID_ROUTE.format(user_id), headers=headers)
    context.result = result
    print(result)


@then('the user info will return successfully')
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    message = ResponseReader.get_body(result)
    print(message)
    assert message["user_name"] == context.user_name.lower()


@then("the user info wont return to not authorized user")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.NOT_AUTHORIZED_ERROR


@then("the user info wont return to not authenticated user")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR


@then("the user info wont return")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR