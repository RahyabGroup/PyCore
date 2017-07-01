from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'R.Azh'


class Type:
    def validate(self, item_to_validate, field_name=None):
        if item_to_validate not in [None, True, False]:
            result = create_result_message(ErrorCodes.TRI_STATE_NOT_VALID, field_name, item_to_validate)
            return result
        return None


