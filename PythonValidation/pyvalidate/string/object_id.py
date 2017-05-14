import re
from pyvalidate.create_result_message import create_result_message
from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class ObjectId:
    def validate(self, item_to_validate, field_name=None):
        object_id_pattern = '^[0-9a-f]{24}'
        #fixme
        if not re.match(object_id_pattern, str(item_to_validate)):
            result = create_result_message(ErrorCodes.OBJECT_ID_NOT_VALID, field_name, item_to_validate)
            return result
        return None
