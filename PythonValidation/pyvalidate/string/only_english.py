import re

from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class OnlyEnglish:
    def validate(self, item_to_validate):
        only_string_pattern = '^[a-zA-Z \n]+$'
        if not re.match(only_string_pattern, item_to_validate):
            result = ErrorCodes.ITEM_IS_NOT_ONLY_ENGLISH
            result["data"] = item_to_validate
            return result
        return None
