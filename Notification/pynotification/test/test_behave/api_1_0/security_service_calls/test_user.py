from pynotification.test.test_behave.resources.constants import Constants
from pynotification.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from bson import ObjectId
from behave import *
import requests

from pynotification.test.test_behave.resources.url_addresses import Url
from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes


@Given('sysadmin registered a user with an email and password - user_create')
def step_impl(context):
    user_dict = {"email": "{}@mailinator.com".format(str(ObjectId())), "password": str(ObjectId())}
    context.email = user_dict["email"]
    context.password = user_dict["password"]
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_CREATE_ROUTE, json=user_dict, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    # message = result.json()["message"]
    message = ResponseReader.get_body(result)
    context.user_id = message
    context.token = result.headers.get("token")


@Given('sysadmin registered user "{username}" with an email and password - user_create')
def step_impl(context, username):
    user_dict = {"email": "{}@mailinator.com".format(username + str(ObjectId())), "password": str(ObjectId())}
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_CREATE_ROUTE, json=user_dict, headers=headers)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    message = ResponseReader.get_body(result)
    print("user id: {}".format(message))
    token = result.headers.get("token")
    user = {"email": user_dict["email"], "password": user_dict["password"], "token": token, "id": message}
    users = getattr(context, "users", None)  # context.users
    if not users:
        context.users = {}
    context.users[username] = user


@Given('a set of specific users')
def step_impl(context):
    users = context.users
    if not users:
        context.users = {}
    for row in context.table:
        user = {"email": row["name"], "password": row["password"]}
        context.users[row["username"]] = user


@Given('sysadmin registered users in list with the emails and passwords - user_create')
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    for user in context.users:
        if user != "sysadmin":
            user_dict = context.users[user]
            user_dict["email"] += (str(ObjectId())) + "@mailinator.com"  # (str(ObjectId()))[:-1:5]
            result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_CREATE_ROUTE, json=user_dict, headers=headers)
            print(result)

            message = ResponseReader.get_body(result)
            # token = result.headers.get("token")
            context.users[user]["id"] = message
            print("\n", message)
            assert result.status_code == ResponseStatusCodes.POST_SUCCESS


@Given('sysadmin activated the user - user_activate')
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.put(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_ACTIVATE_ROUTE.format(context.user_id), headers=headers)
    print(result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS


@Given("sysadmin deactivated the user - user_deactivate")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.put(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_DEACTIVATE_ROUTE.format(context.user_id), headers=headers)
    print(result)
    context.result = result


@Given('sysadmin deactivated the user "{username}" - user_deactivate')
def step_impl(context, username):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.put(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_USER_DEACTIVATE_ROUTE.format(context.users[username]["id"]), headers=headers)
    print(result)
    context.result = result


@Given('we are logged in as sysadmin - login')
def step_impl(context):
    login_dict = {"email": Constants.SYSADMIN_EMAIL, "password": Constants.SYSADMIN_PASS}
    print("\nlogin user: ", login_dict)
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    users = getattr(context, "users", None)  # context.users
    if not users:
        context.users = {}
    context.users["sysadmin"] = {"token": token, "email": Constants.SYSADMIN_EMAIL, "password": Constants.SYSADMIN_PASS, "id": Constants.SYSADMIN_ID}


@Given("we are logged in with the email and password - login")
def step_impl(context):
    login_dict = {"email": context.email, "password": context.password}
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    context.token = result.headers.get("token")


@Given('we are registered and logged in - register')
def step_impl(context):
    user_dict = {"email": "{}@gmail.com".format(str(ObjectId())), "password": str(ObjectId())}
    context.email = user_dict["email"]
    context.password = user_dict["password"]
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_REGISTER_ROUTE, json=user_dict)
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    context.token = token


@Given('user "{username}" is registered and logged in - register')
def step_impl(context, username):
    user_dict = {"email": "{}@gmail.com".format(str(ObjectId())), "password": str(ObjectId())}
    if context.emails is None:
        context.emails = {}
    context.emails[username] = user_dict["email"]
    if context.passwords is None:
        context.passwords = {}
    context.passwords[username] = user_dict["password"]
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_REGISTER_ROUTE, json=user_dict)
    print("response : ", result, "\n")
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    token = result.headers.get("token")
    if context.tokens is None:
        context.tokens = {}
    context.tokens[username] = token


@Given('user "{username}" is logged in - login')
def step_impl(context, username):
    user_info = context.users[username]
    login_dict = {"email": user_info["email"], "password": user_info["password"]}
    result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGIN_ROUTE, json=login_dict)
    print(result)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    context.users[username]["token"] = result.headers.get("token")


@Given('users in the list are logged in with their email and password - login')
def step_impl(context):
    for user in context.users:
        user_dict = context.users[user]
        login_dict = {"email": user_dict["email"], "password": user_dict["password"]}
        result = requests.post(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGIN_ROUTE, json=login_dict)
        print(result)
        assert result.status_code == ResponseStatusCodes.POST_SUCCESS
        context.users[user]["token"] = result.headers.get("token")


@Given("we are logged out of the system - logout")
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given("we logged out of the system as sysadmin - logout")
def step_impl(context):
    headers = {"token": context.users["sysadmin"]["token"]}
    result = requests.delete(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS


@Given('user "{username}" logged out from the system - logout')
def step_impl(context, username):
    headers = {"token": context.users[username]["token"]}
    result = requests.delete(Url.SECURITY_DOMAIN_ADDRESS + Url.SECURITY_DOMAIN_LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS
