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


@when('we subscribe_resource_changed_user')
def step_impl(context):
    resource_dict = {"resource_old_name": context.resourceName, "resource_new_name": str(ObjectId())}
    result = requests.put(Url.DOMAIN_ADDRESS + "/internal/users/claims/resources", json=resource_dict)
    context.result = result
    print(result)


@then('the service will subscribe_resource_changed_user')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
