from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory


@when('we check if the user_id is authorized')
def step_impl(context):
    result = requests.delete(Url.DOMAIN_ADDRESS + "/internal/accounts/token_authorize/{}".format(context.user_id))
    context.result = result
    print(result)


@then('the system will give a token')
def step_impl(context):
    if context.error is False:
        result = context.result
        message = ResponseReader.get_body(result)
        print(message)
        assert result.status_code == client.OK


@when('we give "{wronguser_name}" as user_name and a password')
def step_impl(context, wronguser_name):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(wronguser_name, str(ObjectId()))
    try:
        result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=login_dict)
        context.result = result
        context.error = False
        print("\n test with user_name:", wronguser_name)
        print(result)
    except:
        print("error connecting to server")
        context.error = True


@when('we give our user_name and a "{wrongpassword}" password')
def step_impl(context, wrongpassword):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(context.user_name, wrongpassword)
    try:
        result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=login_dict)
        context.result = result
        context.error = False
        print("\n test with pass:", wrongpassword)
        print(result)
    except:
        print("error connecting to server")
        context.error = True


# @when("we give our user_name and a None password")
# def step_impl(context):
#     instance_factory = UserInstanceFactory()
#     login_dict = instance_factory.create_login_dict(context.user_name, None)
#     try:
#         result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=login_dict)
#         context.result = result
#         context.error = False
#         print(result)
#     except:
#         print("error connecting to server")
#         context.error = True

@when("we give None as user_name and a password")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(None, "some@password")
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=login_dict)
    context.result = result
    print(result)


@then('the system will confirm that user_id is authorized')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("\nmessage: ", message)
    assert result.status_code == client.OK
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
