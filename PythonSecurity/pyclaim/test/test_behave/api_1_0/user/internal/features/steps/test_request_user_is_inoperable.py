from http import client

from behave import *
import requests

from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@given('the user is not active')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict()
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + "/users", json=user_dict)
    print(result)
    assert result.status_code == client.CREATED
    message = result.json()["data"]
    context.user_id = message["_id"]


@when('we check user activation status')
def step_impl(context):
    user_id = context.user_id
    result = requests.get(Url.DOMAIN_ADDRESS + "/internal/users/{}".format(user_id))
    context.result = result
    print(result)


@then('the service will return True')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # assert message[""] == True
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
