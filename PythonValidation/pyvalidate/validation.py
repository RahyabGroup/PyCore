from pyvalidate.exception.validation_exception import ValidationException
from pyvalidate.integer.container import Container as IntegerContainer
from pyvalidate.list.container import Container as ListContainer
from pyvalidate.object.container import Container as CustomContainer
from pyvalidate.string.container import Container as StringContainer
from pyvalidate.datetime.container import Container as DateContainer
from pyvalidate.float.container import Container as FloatContainer
from pyvalidate.boolean.container import Container as BooleanContainer
from pyvalidate.tri_state.container import Container as TriStateContainer

__author__ = 'h.rouhani'


class Validation:
    _validation_result = []
    string = StringContainer(_validation_result)
    integer = IntegerContainer(_validation_result)
    float = FloatContainer(_validation_result)
    list = ListContainer(_validation_result)
    custom = CustomContainer(_validation_result)
    date = DateContainer(_validation_result)
    boolean = BooleanContainer(_validation_result)
    tri_state = TriStateContainer(_validation_result)

    def validate(self):
        if len(self._validation_result) > 0:
            validation_result = self._validation_result.copy()
            self._validation_result.clear()
            raise ValidationException(validation_result)
        return None
