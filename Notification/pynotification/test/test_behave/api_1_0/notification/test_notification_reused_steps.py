from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pynotification.test.test_behave.resources.url_addresses import Url
from pynotification.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'root'
from behave import *
import requests


@when('we send a push notification to the user "{username}" with type "{message_type}" - push')
def step_impl(context, username, message_type):
    # dto = {"receiver_ids": [context.users[username]["id"]], "message_type": message_type, "data": "notify of new something"}
    dto = {"receiver_ids": ['578b8c0de432251528fbb2b8'], "message_type": 'wall-post', "data": "notify of new something"}
    result = requests.post('{}{}'.format(Url.DOMAIN_ADDRESS, Url.PUSH_ROUTE), json=dto)
    context.result = result
    print(result)


@Given('we sent a push notification to the user "{username}" with type "{message_type}" - push')
def step_impl(context, username, message_type):
    dto = {"receiver_ids": [context.users[username]["id"]], "message_type": message_type, "data": "notify of something new"}
    result = requests.post('{}{}'.format(Url.DOMAIN_ADDRESS, Url.PUSH_ROUTE), json=dto)
    context.result = result
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS


@step('we get the notification of user "{username}" with type "{message_type}" - notification_get_by_receiver_id')
def step_impl(context, username, message_type):
    headers = {"token": context.users[username]["token"]}
    query_string = {"skip": 0, "take": 1}
    result = requests.get("{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_GET_BY_RECEIVER_ID_ROUTE.format(context.users[username]["id"], message_type))
                          , params=query_string, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    message = ResponseReader.get_body(result)
    print(message)
    if message:
        for notification in message:
            context.notification_id = notification["_id"]
