import re
from pyvalidate.create_result_message import create_result_message

from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class OnlyEnglish:
    def validate(self, item_to_validate, field_name=None):
        only_string_pattern = '^[a-zA-Z \n]+$'
        if not re.match(only_string_pattern, item_to_validate):
            result = create_result_message(ErrorCodes.ITEM_IS_NOT_ONLY_ENGLISH, field_name, item_to_validate)
            return result
        return None
