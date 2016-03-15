from http import client

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url


@when('we create a resource')
def step_create_a_resource(context):
    resource_dict = {"name": str(ObjectId())}
    headers = {"token": context.token}
    result = requests.post(Url.DOMAIN_ADDRESS + "/resources", json=resource_dict, headers=headers)
    context.result = result
    print(result)


@then('the resource will be added successfully')
def step_impl(context):
    result = context.result
    from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
