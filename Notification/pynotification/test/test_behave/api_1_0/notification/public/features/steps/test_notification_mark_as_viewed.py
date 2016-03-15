from behave import *
import requests

from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pynotification.test.test_behave.resources.url_addresses import Url


@when('we change the notification status to read as user "{username}" _ notification_mark_as_viewed')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    result = requests.put("{}{}".format(Url.DOMAIN_ADDRESS,
                                        Url.NOTIFICATION_MARK_AS_VIEWED_ROUTE.format(context.notification_id)),
                                        headers=headers)
    print(result)
    context.result = result


@then("the notification status will change successfully")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.PUT_SUCCESS


@when(
    'we change the notification status to read as user "{username}" with empty notification id _ notification_mark_as_viewed')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    result = requests.put("{}{}".format(Url.DOMAIN_ADDRESS,
                                        Url.NOTIFICATION_MARK_AS_VIEWED_ROUTE.format("   "))
                          , headers=headers)
    print(result)
    context.result = result


@then("the notification status wont change")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR


@when(
    'we change the notification status to read as user "{username}" with invalid notification id _ notification_mark_as_viewed')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    result = requests.put("{}{}".format(Url.DOMAIN_ADDRESS,
                                        Url.NOTIFICATION_MARK_AS_VIEWED_ROUTE.format(context.users[username]["id"]))
                          , headers=headers)
    print(result)
    context.result = result