from pyvalidate.list.custom import Custom
from pyvalidate.list.size import Size
from pyvalidate.validation_container import ValidationContainer

__author__ = 'h.rouhani'


class Container(ValidationContainer):
    def size(self, list, min_size=None, max_size=None, none_exception=True, field_name=None):
        list_size_validation = Size(min_size, max_size)
        return self._execute(list, list_size_validation, none_exception, field_name)

    def custom(self, list, validation, none_exception=True, field_name=None):
        custom_list_validation = Custom(validation)
        return self._execute(list, custom_list_validation, none_exception, field_name)
