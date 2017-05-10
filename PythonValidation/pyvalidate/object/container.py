from pyvalidate.object.manual import Manual
from pyvalidate.object.custom import Custom
from pyvalidate.validation_container import ValidationContainer

__author__ = 'h.rouhani'


class Container(ValidationContainer):
    def register(self, item_to_validate, validation, none_exception=True, field_name=None):
        custom_validation = Custom(validation)
        return self._execute(item_to_validate, custom_validation, none_exception, field_name)

    def register_async(self, item_to_validate, validation, none_exception=True, field_name=None):
        custom_validation = Custom(validation)
        return (yield from self._execute_async(item_to_validate, custom_validation, none_exception, field_name))

    def manual(self, validation_error_code, none_exception=True, data='', field_name=None):
        manual_validation = Manual(data)
        return self._execute(validation_error_code, manual_validation, none_exception, field_name)
