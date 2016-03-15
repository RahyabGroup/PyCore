from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@Given('we added a claim_type')
def step_create_a_claim_type(context):
    claim_type_dict = {"name": str(ObjectId())}
    context.claimTypeName = claim_type_dict["name"]
    headers = {"token": context.token}
    print("\ncreate a claim_type:", claim_type_dict)
    result = requests.post(Url.DOMAIN_ADDRESS + "/claimtypes", json=claim_type_dict, headers=headers)
    context.result = result
    print(result)
    message = result.json()["data"]
    claimtypedetail = message["ClaimTypeDetail"]
    context.claimTypeId = claimtypedetail["_id"]


@when('we subscribe_claim_type_removed_user')
def step_impl(context):
    result = requests.delete(Url.DOMAIN_ADDRESS + "/internal/users/claims/claim_types/{}".format(context.claimTypeId))
    context.result = result
    print(result)


@then('the service will subscribe_claim_type_removed_user')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
