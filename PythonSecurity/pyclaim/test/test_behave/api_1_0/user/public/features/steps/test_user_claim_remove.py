from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we delete that claim')
def step_impl(context):
    user_id = context.user_id
    headers = {"token": context.token}
    claim_id = context.claimId
    result = requests.delete(Url.DOMAIN_ADDRESS + "/users/{}/claims/{}".format(user_id, claim_id), headers=headers)
    context.result = result
    print(result)


@then('the claim will be deleted successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
