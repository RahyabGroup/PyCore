import dateutil.parser
from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'H.Rouhani'


class AvailableDateString:
    def validate(self, item_to_validate, field_name=None):
        try:
            dateutil.parser.parse(item_to_validate)
            return None
        except:
            result = create_result_message(ErrorCodes.DATE_TIME_STRING_IS_NOT_VALID, field_name, item_to_validate)
            return result
