import re

from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class ObjectId:
    def validate(self, item_to_validate):
        object_id_pattern = '^[0-9a-f]{24}'
        if not re.match(object_id_pattern, item_to_validate):
            result = ErrorCodes.OBJECT_ID_NOT_VALID
            result["data"] = item_to_validate
            return result
        return None
