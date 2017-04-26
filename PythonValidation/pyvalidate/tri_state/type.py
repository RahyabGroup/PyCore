from pyvalidate.resources import ErrorCodes

__author__ = 'root'


class Type:
    def validate(self, item_to_validate):
        if item_to_validate not in [None, True, False]:
            result = ErrorCodes.TRI_STATE_NOT_VALID
            result['data'] = item_to_validate
            return result
        return None


