from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@given('IPN is working')
def step_impl(context):
    pass


@when('sysadmin create a user with an user_name and password - user_create')
def step_impl(context):
    headers = {"token": context.sysadmin_token}
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict()
    # user_dict = instance_factory.create_user_dict_with_user_name_password("r_azh_777@yahoo.com", "12345678")
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@then('the user will be created successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['claim_type_name'] == "USER_NAME"
    context.user_id = message


@when('sysadmin register a user with an already exist user_name - user_create')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict()
    user_dict["user_name"] = context.user_name
    headers = {"token": context.sysadmin_token}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@when('sysadmin register a user with an invalid user_name - user_create')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    headers = {"token": context.sysadmin_token}
    user_dict = instance_factory.create_user_dict_with_user_name_password("testinvaliddddddduser_name", str(ObjectId()))
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@when('sysadmin register a user with an invalid password - user_create')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    headers = {"token": context.sysadmin_token}
    user_dict = instance_factory.create_user_dict_with_user_name_password("{}@gmail.com".format(str(ObjectId())), "1")
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@when('sysadmin register a user with an user_name and a None password - user_create')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    headers = {"token": context.sysadmin_token}
    user_dict = instance_factory.create_user_dict_with_user_name_password("{}@gmail.com".format(str(ObjectId())), None)
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@when('sysadmin register a user with None as user_name and a password - user_create')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    headers = {"token": context.sysadmin_token}
    user_dict = instance_factory.create_user_dict_with_user_name_password(None, str(ObjectId()))
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    context.result = result
    print(result)


@then('the user wont be registered')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    print(result.status_code)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    # assert result.message == 'err1008'  #b'{"data": [{"err1008": ""}]}'

# @given("X is a deleted account")
# def step_impl(context):
#     instance_factory = UserInstanceFactory()
#     user_dict = instance_factory.create_user_dict()
#     context.user_name = user_dict['user_name']
#     result1 = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict)
#     if result1.status_code == client.CREATED:
#         login_dict = instance_factory.create_login_dict(user_dict['user_name'], user_dict['password'])
#         result2 = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=login_dict)
#         token = result2.headers.get("token")
#         # content_json = result2.json()
#         # message = content_json["data"]
#         # headers = message["token"]
#           headers = {"token": context.token}
#         result3 = requests.delete(Url.DOMAIN_ADDRESS + "/users/{}".format(context.user_id), headers=headers)
#         context.token = token
#         print(result3)
#
#
# @when('we register a user with user_name of X')
# def step_impl(context):
#     instance_factory = UserInstanceFactory()
#     user_dict = instance_factory.create_user_dict_with_user_name_password(user_name=context.user_name,password=str(ObjectId()))
#         result1 = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict)
#         context.result = result1

#
# @then('the user X will be registered successfully')
# def step_impl(context):
#         result = context.result
#         content_json = result.json()
#         message = content_json["data"]
#         print(message)
#         print(result.status_code)
#         assert result.status_code == client.CREATED
