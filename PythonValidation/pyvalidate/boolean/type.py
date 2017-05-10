from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class Type:
    def validate(self, item_to_validate, field_name=None):
        if not isinstance(item_to_validate, bool):
            result = create_result_message(ErrorCodes.ITEM_IS_NOT_BOOLEAN, field_name, item_to_validate)
            return result
        return None


