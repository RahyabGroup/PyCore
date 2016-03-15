from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from bson import ObjectId
from behave import *
import requests

from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url
from pyclaim.test.test_behave.api_1_0.user import test_user_reused_steps


@when("we login with the user_name and password - login")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(context.user_name, context.password)
    #login_dict = {"user_name": "bahartest3@chmail.ir", "password": "bahartest2@chmail.ir"}

    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    # token = result2.headers.get("token")
    context.result = result
    print(result)


@then('the system will give us a token')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print(message)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    # assert message == InfoCodes.DONE
    assert result.headers.get("token") is not None


@when('we login with a "{wronguser_name}" as user_name and a password - login')
def step_impl(context, wronguser_name):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(wronguser_name, str(ObjectId()))
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    context.result = result
    print("\n test with user_name:", wronguser_name)
    print(result)


@when('we login with the user_name and a "{wrongpassword}" password - login')
def step_impl(context, wrongpassword):
    instance_factory = UserInstanceFactory()
    login_dict = instance_factory.create_login_dict(context.user_name, wrongpassword)
    result = requests.post(Url.DOMAIN_ADDRESS + Url.LOGIN_ROUTE, json=login_dict)
    context.result = result
    print("\n test with pass:", wrongpassword)
    print(result)


@then('the system wont give us a token')
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
    message = ResponseReader.get_body(result)
    print(message)
