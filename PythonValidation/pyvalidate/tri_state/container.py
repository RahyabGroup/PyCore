from pyvalidate.tri_state.type import Type
from pyvalidate.validation_container import ValidationContainer

__author__ = 'R.Azh'


class Container(ValidationContainer):
    def type(self, item_to_validate, none_exception=True, field_name=None):
        tri_state_type_validation = Type()
        return self._execute(item_to_validate, tri_state_type_validation, none_exception, field_name)

