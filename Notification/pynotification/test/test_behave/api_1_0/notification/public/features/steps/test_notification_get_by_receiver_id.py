from behave import *
import requests

from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pynotification.test.test_behave.resources.url_addresses import Url
from pynotification.test.test_behave.test_utilities.response_reader import ResponseReader


@step('we get the notifications of user "{username}" with type "{message_type}" - notification_get_by_receiver_id')
def step_impl(context, username, message_type):
    headers = {"token": context.users[username]["token"]}
    query_string = {"skip": 0, "take": 10}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], message_type))
                          , params=query_string, headers=headers)
    print(result)
    context.result = result


@then("the list of notifications will return successfully")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.GET_SUCCESS
    message = ResponseReader.get_body(context.result)
    print(message)


@then("the list of notifications wont return to not authenticated user")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR
    message = ResponseReader.get_body(context.result)
    print(message)


@when('we get the notifications of user "{username}" with empty message_type - notification_get_by_receiver_id')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    query_string = {"skip": 0, "take": 10}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], "  "))
                          , params=query_string, headers=headers)
    print(result)
    context.result = result


@then("the list of notifications wont return")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    message = ResponseReader.get_body(context.result)
    print(message)


@when(
    'we get the notifications of user "{username}" with type "{message_type}" and empty query string - notification_get_by_receiver_id')
def step_impl(context, username, message_type):
    headers = {"token": context.users[username]["token"]}
    query_string = {}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], message_type))
                          , params=query_string, headers=headers)
    print(result)
    context.result = result