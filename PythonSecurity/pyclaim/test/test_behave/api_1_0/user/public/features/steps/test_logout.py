from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader
from pyclaim.test.test_behave.api_1_0.user import test_user_reused_steps

__author__ = 'azh'

from behave import *
import requests

from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url


@when("we log out from the system - logout")
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result


@then('we will be logged out successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS
    # assert message == InfoCodes.DONE


@when("we log out from the system with the same token - logout")
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
    print("\nresult : ", result)
    context.result = result

# @when("we log out from the system with a random token")
# def step_impl(context):
#     headers = {"token": str(ObjectId())}
#     result = requests.delete(Url.DOMAIN_ADDRESS + Url.LOGOUT_ROUTE, headers=headers)
#     print("\nresult : ", result)
#     context.result = result
