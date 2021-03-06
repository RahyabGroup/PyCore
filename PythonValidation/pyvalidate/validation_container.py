from pyvalidate.resources import ErrorCodes

__author__ = 'Hooman'


class ValidationContainer:
    def __init__(self, validation_result):
        self._validation_result = validation_result

    def _execute(self, item_to_validate, validator, none_exception, field_name=None):
        if item_to_validate is None:
            if none_exception:
                result = ErrorCodes.ITEM_IS_NONE.copy()
                result[field_name if field_name else "data"] = ""
                none_validation_error = result
                self._validation_result.append(none_validation_error)
                return [none_validation_error]
            else:
                return None
        result = validator.validate(item_to_validate, field_name)
        if result is not None:
            if isinstance(result, list):
                self._validation_result.extend(result)
            else:
                self._validation_result.append(result)
        return result

    def _execute_async(self, item_to_validate, validator, none_exception, field_name=None):
        if item_to_validate is None:
            if none_exception:
                result = ErrorCodes.ITEM_IS_NONE
                result[field_name if field_name else "data"] = ""
                none_validation_error = result
                self._validation_result.append(none_validation_error)
                return [none_validation_error]
            else:
                return None
        result = yield from validator.validate(item_to_validate, field_name)
        if result is not None:
            if isinstance(result, list):
                self._validation_result.extend(result)
            else:
                self._validation_result.append(result)
        return result
