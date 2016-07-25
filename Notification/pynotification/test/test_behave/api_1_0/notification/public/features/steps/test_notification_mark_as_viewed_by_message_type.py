from behave import *
import requests
from pynotification.test.test_behave.resources.url_addresses import Url


@when(
    'we change the notification status to read as user "{user_name}" with type "{message_type}" _ '
    'notification_mark_as_viewed')
def step_impl(context, user_name, message_type):
    headers = {"token": context.users[user_name]["token"]}
    result = requests.put("{}{}".format(Url.DOMAIN_ADDRESS,
                                        Url.NOTIFICATION_MARK_AS_VIEWED_BY_MESSAGE_TYPE_ROUTE.format(message_type))
                          , headers=headers)
    print(result)
    context.result = result