from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Size:
    def __init__(self, min_value=None, max_value=None):
        self._min_value = min_value
        self._max_value = max_value

    def validate(self, item_to_validate, field_name=None):
        if self._min_value is not None:
            if item_to_validate < self._min_value:
                message = "{} < {}".format(item_to_validate, self._min_value)
                result = create_result_message(ErrorCodes.INTEGER_LOWER_THAN_MIN_SIZE, field_name, message)
                return result

        if self._max_value is not None:
            if item_to_validate > self._max_value:
                message = "{} > {}".format(item_to_validate, self._max_value)
                result = create_result_message(ErrorCodes.INTEGER_HIGHER_THAN_MAX_SIZE, field_name, message)
                return result
        return None
