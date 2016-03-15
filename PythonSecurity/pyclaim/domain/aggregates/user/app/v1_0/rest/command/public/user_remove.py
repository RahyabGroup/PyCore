from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_remove_container import \
    UserRemoveContainer
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserRemoveContainer)
class UserRemove:
    _id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = self._id
        user.remove()
        return "Done"
