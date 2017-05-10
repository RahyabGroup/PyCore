from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Positive:
    def __init__(self, include_zero=True):
        self._include_zero = include_zero

    def validate(self, item_to_validate, field_name=None):
        if item_to_validate < 0 or (not self._include_zero and item_to_validate == 0):
            result = create_result_message(ErrorCodes.ITEM_IS_NOT_POSITIVE, field_name, item_to_validate)
            return result
        return None
