from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url

@given('we have a claim_type')
def step_create_a_claim_type(context):
    claim_type_dict = {"name": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.post(Url.DOMAIN_ADDRESS + "/claimtypes", json=claim_type_dict, headers=headers)
    context.result = result
    assert result.status_code == client.OK
    message = result.json()["data"]
    claimtypedetail = message["ClaimTypeDetail"]
    context.claimTypeId = claimtypedetail["_id"]  # ?????????????????????????
    print(result)


@when('we add a claim for that resource with the claim_type')
def step_impl(context):
    claim_dict = {"claim_type_id": context.claimTypeId, "claim_value": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.put(Url.DOMAIN_ADDRESS + "/resources/{}/claims".format(context.resourceId), claim_dict, headers=headers)
    context.result = result
    print(result)

    try:
        result = requests.put(Url.DOMAIN_ADDRESS + "/resources/%s/claims", context.resourceId, claim_dict,
                              headers=headers)
        context.result = result
        print(result)
        context.error = False
    except:
        print("error connecting to server")
        context.error = True


@then('the claim will be added to resource successfully')
def step_impl(context):
    result = context.result
    from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader
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
