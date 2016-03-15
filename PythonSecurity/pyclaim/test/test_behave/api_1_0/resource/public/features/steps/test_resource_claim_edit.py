from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@Given('we have a claim with that claim_type in resource')
def step_impl(context):
    claim_dict = {"claim_type_id": context.claimTypeId, "claim_value": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.put(Url.DOMAIN_ADDRESS + "/resources/{}/claims".format(context.resourceId), claim_dict, headers=headers)
    result = requests.put(Url.DOMAIN_ADDRESS + "/resources/%s/claims", context.resourceId, claim_dict,
                          headers=headers)
    assert result.status_code == client.OK
    message = result.json()["data"]
    claimdetail = message["ClaimDetail"]
    context.claimId = claimdetail["_id"]


@when('we edit that claim of the resource')
def step_impl(context):
    claim_dict = {"claim_type_id": context.claimTypeId, "claim_value": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.put(Url.DOMAIN_ADDRESS + "/resources/{}/claims/{}".format(context.resourceId, context.claimId), claim_dict, headers=headers)
    context.result = result
    print(result)
    try:
        result = requests.put(Url.DOMAIN_ADDRESS + "/resources/%s/claims/%s", context.resourceId,
                              context.claimId, claim_dict, headers=headers)
        context.result = result
        print(result)
        context.error = False
    except:
        print("error connecting to server")
        context.error = True


@then('the claim will be edited successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO

    if context.error is False:
        result = context.result
        message = ResponseReader.get_body(result)
        print(message)
        assert result.status_code == client.OK
        # TO DO
        # assert message["user_name"] == context.user_name
        # assert message["claims"][0]['name'] == "USER_NAME"
