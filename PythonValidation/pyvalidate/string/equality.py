from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Equality:
    compare_with = None

    def __init__(self, compare_with):
        self.compare_with = compare_with

    def validate(self, item_to_validate, field_name=None):
        if item_to_validate == self.compare_with:
            message = "{} is not equal with {}".format(item_to_validate, self.compare_with)
            result = create_result_message(ErrorCodes.ITEMS_ARE_NOT_EQUAL, field_name, message)
            return result
