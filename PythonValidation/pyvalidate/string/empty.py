from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Empty:
    def validate(self, item_to_validate, field_name=None):
        if not item_to_validate.strip():
            result = create_result_message(ErrorCodes.STRING_IS_EMPTY_OR_NULL, field_name, '')
            return result