import re
from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'h.rouhani'


class Email:
    def validate(self, item_to_validate, field_name=None):
        email_pattern = "[^@]+@[^@]+\.[^@]+"
        if not re.match(email_pattern, item_to_validate):
            result = create_result_message(ErrorCodes.EMAIL_NOT_VALID, field_name, item_to_validate)
            return result
        return None
