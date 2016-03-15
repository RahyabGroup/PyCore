from http import client

from bson import ObjectId
from behave import *
import requests
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader
from pyclaim.test.test_behave.api_1_0.user import test_user_reused_steps


@when('we create a claim_type as user "{user_name}" - claim_type_create')
def step_create_a_claim_type(context, user_name):
    claim_type_dict = {"name": str(ObjectId())}
    headers = {"token": context.users[user_name]["token"]}
    result = requests.post("{}{}".format(Url.DOMAIN_ADDRESS, Url.CLAIM_TYPE_CREATE_ROUTE), json=claim_type_dict, headers=headers)
    context.claim_type_name = claim_type_dict["name"]
    context.result = result
    print(result)


@then('the claim_type will be added successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    # claimtypedetail = message["ClaimTypeDetail"]
    # context.claimTypeId = claimtypedetail["_id"]        #?????????????????????????
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"


@then("the claim_type wont create")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR


@then("the claim_type wont create for not authorized user")
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.NOT_AUTHORIZED_ERROR



@when('we create a claim_type with duplicate name as user "{user_name}" - claim_type_create')
def step_impl(context, user_name):
    claim_type_dict = {"name": context.claim_type_name}
    headers = {"token": context.users[user_name]["token"]}
    result = requests.post("{}{}".format(Url.DOMAIN_ADDRESS, Url.CLAIM_TYPE_CREATE_ROUTE), json=claim_type_dict, headers=headers)
    context.result = result
    print(result)


@when('we create a claim_type with empty name as user "{user_name}" - claim_type_create')
def step_impl(context, user_name):
    claim_type_dict = {"name": ""}
    headers = {"token": context.users[user_name]["token"]}
    result = requests.post("{}{}".format(Url.DOMAIN_ADDRESS, Url.CLAIM_TYPE_CREATE_ROUTE), json=claim_type_dict, headers=headers)
    context.result = result
    print(result)