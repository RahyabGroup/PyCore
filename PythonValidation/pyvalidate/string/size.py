from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Size:
    def __init__(self, min_size=None, max_size=None):
        self._min_value = min_size
        self._max_value = max_size

    def validate(self, item_to_validate, field_name=None):
        striped_item = item_to_validate.strip(' ')
        if self._min_value is not None:
            if len(striped_item) < self._min_value:
                message = "{}({})".format(item_to_validate, self._min_value)
                result = create_result_message(ErrorCodes.STRING_SIZE_LOWER_THAN_MIN_SIZE, field_name, message)
                return result

        if self._max_value is not None:
            if len(striped_item) > self._max_value:
                message = "{}({})".format(item_to_validate, self._max_value)
                result = create_result_message(ErrorCodes.STRING_SIZE_HIGHER_THAN_MAX_SIZE, field_name, message)
                return result

        return None
