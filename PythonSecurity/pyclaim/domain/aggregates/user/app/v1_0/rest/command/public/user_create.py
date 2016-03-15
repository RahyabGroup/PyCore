from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_create_container import \
    UserCreateContainer
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserCreateContainer)
class UserCreate:
    user_name = None
    password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user.user_name = self.user_name.lower()
        user.password = self.password
        user.create()
        return user._id
