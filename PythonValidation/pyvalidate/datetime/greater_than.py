from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class GreaterThan:
    def __init__(self, item_to_compare_against, check_equality=False):
        self._item_to_compare_against = item_to_compare_against
        self._check_equality = check_equality

    def validate(self, item_to_validate, field_name=None):
        if self._check_equality:
            if item_to_validate < self._item_to_compare_against:
                message = "{} < {}".format(item_to_validate, self._item_to_compare_against)
                result = create_result_message(ErrorCodes.DATE_TIME_IS_NOT_GREATER, field_name, message)
                return result
        else:
            if item_to_validate <= self._item_to_compare_against:
                message = "{} <= {}".format(item_to_validate, self._item_to_compare_against)
                result = create_result_message(ErrorCodes.DATE_TIME_IS_NOT_GREATER, field_name, message)
                return result


