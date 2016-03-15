from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@given('we have a claim_type')
def step_create_a_claim_type(context):
    claim_type_dict = {"name": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.post(Url.DOMAIN_ADDRESS + "/claimtypes", json=claim_type_dict, headers=headers)
    context.result = result
    assert result.status_code == client.OK
    message = result.json()["data"]
    claimtypedetail = message["ClaimTypeDetail"]
    context.claimTypeId = claimtypedetail["_id"]
    print(result)


@when('we subscribe claim_type removed resource')
def step_create_a_claim_type(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + "//internal/resources/claims/claim_types/{}".format(context.claimTypeId), headers=headers)
    context.result = result
    print(result)


@then('the claim_type will be removed successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
