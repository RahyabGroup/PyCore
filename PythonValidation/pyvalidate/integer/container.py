from pyvalidate.integer.equality import Equality
from pyvalidate.integer.negative import Negative
from pyvalidate.integer.positive import Positive
from pyvalidate.integer.size import Size
from pyvalidate.validation_container import ValidationContainer

__author__ = 'h.rouhani'


class Container(ValidationContainer):
    def size(self, int_value, min_value=None, max_value=None, none_exception=True, field_name=None):
        int_size_validation = Size(min_value, max_value)
        return self._execute(int_value, int_size_validation, none_exception, field_name)

    def positive(self, int_value, include_zero=True, none_exception=True, field_name=None):
        positive_validation = Positive(include_zero)
        return self._execute(int_value, positive_validation, none_exception, field_name)

    def negative(self, int_value, include_zero=True, none_exception=True, field_name=None):
        negative_validation = Negative(include_zero)
        return self._execute(int_value, negative_validation, none_exception, field_name)

    def equality(self, int_value, compare_with, none_exception=True, field_name=None):
        integer_equality_validator = Equality(compare_with)
        return self._execute(int_value, integer_equality_validator, none_exception, field_name)
