from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we edit our user_name and password - user_edit')
def step_impl(context):
    user_dict = {"user_name": "edited_{}@gmail.com".format(str(ObjectId())), "password": str(ObjectId())}
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    headers = {"token": context.token}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_EDIT_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@When('sysadmin edit his user_name to "{user_name}" and password to "{password}" - user_edit')
def step_impl(context, user_name, password):
    user_dict = {"user_name": user_name, "password": password}
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    headers = {"token": context.sysadmin_token}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_EDIT_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@Then('sysadmin edit his user_name to "{user_name}" and password to "{password}" - user_edit')
def step_impl(context, user_name, password):
    user_dict = {"user_name": user_name, "password": password}
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    headers = {"token": context.sysadmin_token}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_EDIT_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS


@then('the user_name and password will change successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS
    # assert message["user_name"] == context.user_name # "edited" in message["user_name"]
    # assert message["claims"][0]['claim_type_name'] == "USER_NAME"


@Then('the user_name and password wont change')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHENTICATED_ERROR


@When('sysadmin changes his user_name to user "{user_name}" user_name - user_edit')
def step_impl(context, user_name):
    user_dict = {"user_name": context.users[user_name]["user_name"], "password": str(ObjectId())}
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_EDIT_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@Then('the user_name wont change')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR


@Then('the user_name and password wont change for not authorized user')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHORIZED_ERROR