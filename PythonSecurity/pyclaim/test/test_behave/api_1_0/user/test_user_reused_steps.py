from pyclaim.test.test_behave.resources.constants import Constants
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url


@Given('sysadmin registered a user with an user_name and password _ user_create')  # ('the user is registered')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    user_dict = instance_factory.create_user_dict()
    context.user_name = user_dict["user_name"]
    context.password = user_dict["password"]
    headers = {"token": context.sysadmin_token}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = result.json()["data"]
    context.user_id = message


@Given('sysadmin registered user "{user_name}" with an user_name and password - user_create')
def step_impl(context, user_name):
    user_dict = {"user_name": "{}@gmail.com".format(user_name + str(ObjectId())), "password": str(ObjectId())}
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = result.json()["data"]
    token = result.headers.get("token")
    user = {"user_name": user_dict["user_name"], "password": user_dict["password"], "token": token, "id": message}
    users = getattr(context, "users", None)  # context.users
    if not users:
        context.users = {}
    context.users[user_name] = user
    context.user_name = user["user_name"]


@Given('sysadmin activated the user - user_activate')
def step_impl(context):
    headers = {"token": context.sysadmin_token}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_ACTIVATE_ROUTE.format(context.user_id), headers=headers)
    print(result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS


@Given('sysadmin deactivated the user - user_deactivate')
def step_impl(context):
    headers = {"token": context.sysadmin_token}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_DEACTIVATE_ROUTE.format(context.user_id), headers=headers)
    print(result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS


@Given('sysadmin created user "{user_name}" with an user_name and password - user_create')
def step_impl(context, user_name):
    user_dict = {"user_name": "{}@gmail.com".format(user_name + str(ObjectId())), "password": str(ObjectId())}
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.USER_CREATE_ROUTE, json=user_dict, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = result.json()["data"]
    token = result.headers.get("token")
    user = {"user_name": user_dict["user_name"], "password": user_dict["password"], "token": token, "id": message}
    users = getattr(context, "users", None)  # context.users
    if not users:
        context.users = {}
    context.users[user_name] = user


@Given("we are logged in with the user_name and password - login")
def step_impl(context):
    login_dict = {"user_name": context.user_name, "password": context.password}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    context.token = result.headers.get("token")


@Given('sysadmin deactivated the user "{user_name}" - user_deactivate')
def step_impl(context, user_name):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.USER_DEACTIVATE_ROUTE.format(context.users[user_name]["id"]), headers=headers)
    print(result)
    context.result = result


@Given('user "{user_name}" registered with an user_name and password - register')
def step_impl(context, user_name):
    instance_factory = UserInstanceFactory()
    register_dict = instance_factory.create_user_dict()
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
    context.result = result
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = ResponseReader.get_body(result)
    token = result.headers.get("token")
    user = {"user_name": register_dict["user_name"], "password": register_dict["password"], "token": token, "id": message}
    users = getattr(context, "users", None)
    if not users:
        context.users = {}
    context.users[user_name] = user


@Given("we logged in with the user_name and password - login")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_user_dict_with_user_name_password(context.user_name, context.password)
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    context.result = result
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    context.token = result.headers.get("token")


@Given("we are logged in as sysadmin - login")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(Constants.SYSADMIN_USER_NAME, Constants.SYSADMIN_PASS)
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    context.sysadmin_token = token
    users = getattr(context, "users", None)  # context.users
    if not users:
        context.users = {}
    context.users["sysadmin"] = {"token": token, "user_name": Constants.SYSADMIN_USER_NAME, "password": Constants.SYSADMIN_PASS, "id": Constants.SYSADMIN_ID}
    context.user_name = Constants.SYSADMIN_USER_NAME


@Given('we are registered and logged in - register')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    register_dict = instance_factory.create_user_dict()
    context.user_name = register_dict["user_name"]
    context.password = register_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    context.token = token


@Given('we have an not authenticated token')
def step_impl(context):
    instance_factory = UserInstanceFactory()
    register_dict = instance_factory.create_user_dict()
    context.user_name = register_dict["user_name"]
    context.password = register_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    context.token = token


@Given("we logged out from the system - logout")
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given('user "{user_name}" is registered and logged in')
def step_impl(context, user_name):
    user_dict = {"user_name": "{}@mailinator.com".format(str(ObjectId())), "password": str(ObjectId())}
    if context.user_names is None:
        context.user_names = {}
    context.user_names[user_name] = user_dict["user_name"]
    if context.passwords is None:
        context.passwords = {}
    context.passwords[user_name] = user_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=user_dict)
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    if context.tokens is None:
        context.tokens = {}
    context.tokens[user_name] = token


@Given('user "{user_name}" is logged in - login')
def step_impl(context, user_name):
    user_info = context.users[user_name]
    login_dict = {"user_name": user_info["user_name"], "password": user_info["password"]}
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    context.users[user_name]["token"] = result.headers.get("token")


@Given('user "{user_name}" logged out from the system - logout')
def step_impl(context, user_name):
    headers = {"token": context.users[user_name]["token"]}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given("we logged out of the system as sysadmin - logout")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given("we logged out from the system as sysadmin - logout")
def step_impl(context):
    headers = {"token": context.sysadmin_token}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given("we register with our user_name and password")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    register_dict = instance_factory.create_user_dict()
    context.user_name = register_dict["user_name"]
    context.password = register_dict["password"]
    result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
    context.result = result
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS

