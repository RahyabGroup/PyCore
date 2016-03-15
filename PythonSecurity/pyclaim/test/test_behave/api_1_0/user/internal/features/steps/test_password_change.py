from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'
from bson import ObjectId
from behave import *
import requests
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.api_1_0.user import test_user_reused_steps
__author__ = 'root'


@when('we change our password - password_change')
def step_impl(context):
    headers = {"token": context.token}
    pass_dict = {"old_password": context.password, "new_password": str(ObjectId())}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.PASSWORD_CHANGE_ROUTE.format(context.user_id), json=pass_dict, headers=headers)
    context.result = result
    print(result)


@then('the password will be changed successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("\nmessage: ", message)
    assert result.status_code == ResponseStatusCodes.GET_SUCCESS


@when("we change our password with wrong old password - password_change")
def step_impl(context):
    headers = {"token": context.token}
    pass_dict = {"old_password": str(ObjectId()), "new_password": str(ObjectId())}
    result = requests.put(Url.DOMAIN_ADDRESS + Url.PASSWORD_CHANGE_ROUTE.format(context.user_id), json=pass_dict, headers=headers)
    context.result = result
    print(result)


@then("the password wont be changed")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("\nmessage: ", message)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR