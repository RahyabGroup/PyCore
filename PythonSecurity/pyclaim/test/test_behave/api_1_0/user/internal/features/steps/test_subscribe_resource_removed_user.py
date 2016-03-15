from http import client

from behave import *
import requests

from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader


@when('we subscribe_resource_removed_user')
def step_impl(context):
    resource_dict = {"resource_name": context.resourceName}
    result = requests.delete(Url.DOMAIN_ADDRESS + "/internal/users/claims/resources", json=resource_dict)
    context.result = result
    print(result)


@then('the service will subscribe_resource_removed_user')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == client.OK
    # TO DO
