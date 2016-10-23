from behave import *
from pyclaim.test.test_behave.resources.response_status_codes import ResponseStatusCodes


@then("user will be activated successfully")
def step_impl(context):
    result = context.result
    print(result)
    assert result.status_code == ResponseStatusCodes.PUT_SUCCESS