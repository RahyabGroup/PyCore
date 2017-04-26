from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class Type:
    def validate(self, item_to_validate):
        if not isinstance(item_to_validate, bool):
            result = ErrorCodes.ITEM_IS_NOT_BOOLEAN
            result['data'] = item_to_validate
            return result
        return None


