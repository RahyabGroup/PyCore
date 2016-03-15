from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@Given('we added a resource')
def step_impl(context):
    resource_dict = {"name": str(ObjectId())}
    context.resourceName = resource_dict["name"]
    headers = {"token": context.token}
    result = requests.post(Url.DOMAIN_ADDRESS + "/resources", json=resource_dict, headers=headers)
    context.result = result
    print(result)
    message = result.json()["data"]
    resourcedetail = message["ResourceTypeDetail"]
    context.resourceId = resourcedetail["_id"]
    context.resourceId = resourcedetail["_id"]


@when('we remove that resource')
def step_impl(context):
    headers = {"token": context.token}
    result = requests.delete(Url.DOMAIN_ADDRESS + "/resources/{}".format(context.resourceId), headers=headers)
    context.result = result
    print(result)


@then('the resource will be removed successfully')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
    # assert message["user_name"] == context.user_name
    # assert message["claims"][0]['name'] == "USER_NAME"
    if context.error is False:
        result = context.result
        message = ResponseReader.get_body(result)
        print(message)
        assert result.status_code == client.OK
        # TO DO
        # assert message["user_name"] == context.user_name
        # assert message["claims"][0]['name'] == "USER_NAME"
