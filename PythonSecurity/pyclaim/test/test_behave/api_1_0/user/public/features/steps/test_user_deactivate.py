from behave import *
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes


@then("user will be deactivated successfully")
def step_impl(context):
    result = context.result
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS