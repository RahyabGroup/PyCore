from behave import *
import requests

from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('sysadmin removes the user account - user_remove')
def step_impl(context):
    user_id = context.user_id
    user_dict = {"_id": user_id}
    headers = {"token": context.sysadmin_token}
    result = requests.delete(Url.DOMAIN_ADDRESS + Url.USER_REMOVE_ROUTE.format(user_id), json=user_dict, headers=headers)
    context.result = result
    print(result)


@then('the account will be removed successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.DELETE_SUCCESS

