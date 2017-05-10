from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Size:
    def __init__(self, min_size=None, max_size=None):
        self._min_value = min_size
        self._max_value = max_size

    def validate(self, item_to_validate, field_name=None):
        list_size = len(item_to_validate)
        if self._min_value is not None:
            if list_size < self._min_value:
                message = "{} < {}".format(list_size, self._min_value)
                result = create_result_message(ErrorCodes.LIST_SIZE_LOWER_THAN_MIN_SIZE, field_name, message)
                return result

        if self._max_value is not None:
            if list_size > self._max_value:
                message = "{} > {}".format(list_size, self._max_value)
                result = create_result_message(ErrorCodes.LIST_SIZE_HIGHER_THAN_MAX_SIZE, field_name, message)
                return result

        return None
