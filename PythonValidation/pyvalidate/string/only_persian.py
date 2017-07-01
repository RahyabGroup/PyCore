import re
import string
from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'R.Azh'


class OnlyPersian:
    def validate(self, item_to_validate, field_name=None):
        farsi_alef_char = chr(1570)
        farsi_ye_char = chr(1740)
        punc = '\\' + '\\'.join(string.punctuation)
        only_persian_string_pattern = '^[{} 0-9 {}-{} \n]+$'.format(punc, farsi_alef_char,
                                                                    farsi_ye_char)
        if not re.match(only_persian_string_pattern, item_to_validate):
            result = create_result_message(ErrorCodes.ITEM_IS_NOT_ONLY_PERSIAN, field_name, item_to_validate)
            return result
        return None
