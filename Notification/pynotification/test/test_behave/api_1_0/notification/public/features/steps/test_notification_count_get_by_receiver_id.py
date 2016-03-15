from behave import *
import requests

from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pynotification.test.test_behave.resources.url_addresses import Url
from pynotification.test.test_behave.api_1_0.security_service_calls import test_user
from pynotification.test.test_behave.api_1_0.notification import test_notification_reused_steps
from pynotification.test.test_behave.test_utilities.response_reader import ResponseReader


@then("the list of notifications count will return successfully")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.GET_SUCCESS
    message = ResponseReader.get_body(context.result)
    print(message)
    assert message == 3


@step('we get the notifications count of user "{username}" with type "{message_type}" - notification_count_get_by_receiver_id')
def step_impl(context, username, message_type):
    headers = {"token": context.users[username]["token"]}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_COUNT_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], message_type))
                          , headers=headers)
    print(result)
    context.result = result


@then("the list of notifications count wont return to not authenticated user")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR
    message = ResponseReader.get_body(context.result)
    print(message)


@when(
    'we get the notifications count of user "{username}" with empty message type - notification_count_get_by_receiver_id')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_COUNT_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], " ")),
                                        headers=headers)
    print(result)
    context.result = result


@then("the list of notifications count wont return")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    message = ResponseReader.get_body(context.result)
    print(message)