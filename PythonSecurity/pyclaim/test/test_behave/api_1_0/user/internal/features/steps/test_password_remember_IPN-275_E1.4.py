from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'
from bson import ObjectId
from behave import *
import requests
from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.url_addresses import Url


@when('we tell the system that the password is forgotten for our user_name - password_remember')
def step_impl(context):
    username_dict = {"user_name": context.user_name}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.PASSWORD_REMEMBER_ROUTE, params=username_dict)
    context.result = result
    print(result)


@when('we tell the system that the password is forgotten with invalid user_name - password_remember')
def step_impl(context):
    username_dict = {"user_name": "{}@mailinator.com".format(str(ObjectId()))}
    result = requests.get(Url.DOMAIN_ADDRESS + Url.PASSWORD_REMEMBER_ROUTE, params=username_dict)
    context.result = result
    print(result)


@then('the system will send an user_name with link to reset password')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("\nmessage: ", message)
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"


@when('we tell the system that the password is forgotten for an invalid user_name - password_remember')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict_with_user_name_password("testinvaliduser_name", str(ObjectId()))
    context.user_name = user_dict["user_name"]
    result = requests.get(Url.DOMAIN_ADDRESS + Url.PASSWORD_REMEMBER_ROUTE, params=user_dict)
    context.result = result
    print(result)


@then('the system will give an error')
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    message = ResponseReader.get_body(result)
    print(message)


@when('we tell the system that the password is forgotten for None as user_name')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict_with_user_name_password(None, str(ObjectId()))
    context.user_name = user_dict["user_name"]
    result = requests.get(Url.DOMAIN_ADDRESS + Url.PASSWORD_REMEMBER_ROUTE, json=user_dict)
    context.result = result
    print(result)


@then("the system will send us the password in clear text")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS


@then("the password wont send to us")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR