import re
import string
from pyvalidate.create_result_message import create_result_message

from pyvalidate.resources import ErrorCodes

__author__ = 'R.Azh'


class OnlyEnglish:
    def validate(self, item_to_validate, field_name=None):
        punc = '\\' + '\\'.join(string.punctuation)
        only_english_string_pattern = '^[{} 0-9a-zA-Z \n]+$'.format(punc)
        if not re.match(only_english_string_pattern, item_to_validate):
            result = create_result_message(ErrorCodes.ITEM_IS_NOT_ONLY_ENGLISH, field_name, item_to_validate)
            return result
        return None
