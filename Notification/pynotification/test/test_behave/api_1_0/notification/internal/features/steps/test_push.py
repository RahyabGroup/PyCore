from behave import *

from pynotification.test.test_behave.resources.response_status_codes import ResponseStatusCodes
from pynotification.test.test_behave.api_1_0.security_service_calls import test_user
from pynotification.test.test_behave.api_1_0.notification import test_notification_reused_steps

@given("notificatin is up")
def step_impl(context):
    pass


@then("the request will be send successfully")
def step_impl(context):
    assert context.result.status_code == ResponseStatusCodes.POST_SUCCESS


