import threading
import time

from behave import *
from pyutil.serialization.json.deserializer import Deserializer

from pynotification.test.test_behave.resources.url_addresses import Url
from sseclient import SSEClient


# import thread


@when('user "{username}" subscribes for notifications with type "{message_type}" from server - subscribe')
def step_impl(context, username, message_type):
    url = "{}{}".format(Url.DOMAIN_ADDRESS, Url.NOTIFICATION_SUBSCRIBE.format(context.users[username]["id"],  message_type))

    def get_notifications(url):
        # session = requests.Session()
        messages = SSEClient(url) #, session=session)
        for message in messages:
            print(message.data.__str__())
            context.message = message.data
            # session.close()

    thread1 = threading.Thread(target=get_notifications, args=(url,))
    thread1.start()
    time.sleep(2)
    context.execute_steps(u"""When we send a push notification to the user "{username}" with type "{message_type}" - push""".format(username=username, message_type=message_type))
    time.sleep(7)
    print(context.message)


@then('the notifications will be received for user "{username}" successfully')
def step_impl(context, username):
    # message_data = context.message.strip('[]')
    json_deserializer = Deserializer()
    data = json_deserializer.deserialize_from_string(context.message)
    assert data[0]["receiver_id"] == context.users[username]["id"]
