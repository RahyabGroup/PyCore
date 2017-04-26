from pyvalidate.boolean.type import Type
from pyvalidate.validation_container import ValidationContainer

__author__ = 'root'


class Container(ValidationContainer):
    def type(self, item_to_validate, none_exception=True):
        tri_state_type_validation = Type()
        return self._execute(item_to_validate, tri_state_type_validation, none_exception)



