from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class TextSize:
    def __init__(self, min_size=None, max_size=None):
        self._min_value = min_size
        self._max_value = max_size

    def validate(self, item_to_validate, field_name=None):
        striped_item = item_to_validate.strip(' ')

        if self._min_value is not None:
            if len(striped_item.split('\n', self._min_value)) < self._min_value and len(striped_item.split(' ', self._min_value)) < self._min_value:
                message = "{}({})".format(item_to_validate, self._min_value)
                result = create_result_message(ErrorCodes.TEXT_WORDS_LOWER_THAN_MIN, field_name, message)
                return result

        if self._max_value is not None:
            if len(striped_item.split('\n', self._max_value + 1)) > self._max_value and len(striped_item.split(' ', self._max_value + 1)) > self._max_value:
                message = "{}({})".format(item_to_validate, self._max_value)
                result = create_result_message(ErrorCodes.TEXT_WORDS_HIGHER_THAN_MAX, field_name, message)
                return result

        return None
