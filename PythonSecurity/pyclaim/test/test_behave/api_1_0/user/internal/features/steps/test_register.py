from pyclaim.test.test_behave.test_utilities.response_reader import ResponseReader

__author__ = 'azh'

from behave import *
import requests

from pyclaim.test.test_behave.api_1_0.user.user_instance_factory import UserInstanceFactory
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pyclaim.test.test_behave.resources.url_addresses import Url

@given('Security is working')
def step_impl(context):
    pass


@when("we register with our user_name and password - register")
def step_impl(context):
    instance_factory = UserInstanceFactory()
    register_dict = instance_factory.create_user_dict()
    context.user_name = register_dict["user_name"]
    result = requests.post("{}{}".format(Url.DOMAIN_ADDRESS, Url.REGISTER_ROUTE), json=register_dict)
    context.result = result
    print("response : ", result, "\n")


@then('the system will give a token after register')
def step_impl(context):
    result = context.result
    message = ResponseReader.get_body(result)
    print("message : ", message)
    assert result.status_code == ResponseStatusCodes.POST_SUCCESS
    assert result.headers.get("token") is not None

#
#
# @when('we register with our user_name and an "{invalid_password}" - register')
# def step_impl(context, invalid_password):
#     instance_factory = UserInstanceFactory()
#     register_dict = instance_factory.create_user_dict_with_user_name_password("{}@gmail.com".format(str(ObjectId())), invalid_password)
#     result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
#     context.result = result
#     print("response : ", result, "\n")
#
#
# @when('we register with "{invalid_user_name}" as user_name and a password - register')
# def step_impl(context, invalid_user_name):
#     instance_factory = UserInstanceFactory()
#     register_dict = instance_factory.create_user_dict_with_user_name_password(invalid_user_name, str(ObjectId()))
#     result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
#     context.result = result
#     print("response : ", result, "\n")
#
#
# @when('we register again with the same user_name and a password - register')
# def step_impl(context):
#     instance_factory = UserInstanceFactory()
#     register_dict = instance_factory.create_user_dict_with_user_name_password(context.user_name, str(ObjectId()))
#     result = requests.post(Url.DOMAIN_ADDRESS + Url.REGISTER_ROUTE, json=register_dict)
#     context.result = result
#     print("response : ", result, "\n")
#
#
# @Given("we register again with the same user_name and a password - register")
# def step_impl(context):
#     context.execute_steps(u'we register again with the same user_name and a password')
#     # we register with our user_name {} password
#     # """.format("and"))
#
#
# @then('the system wont give a token after register')
# def step_impl(context):
#     result = context.result
#     message = ResponseReader.get_body(result)
#     print("message : ", message)
#     assert result.status_code == ResponseStatusCodes.BAD_REQUEST_ERROR
