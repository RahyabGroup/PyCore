from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_edit_container import \
    UserEditContainer
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator, auth

__author__ = 'Hooman'


@validator.validation(UserEditContainer)
class UserEdit:
    user_name = None
    password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = auth.user_id
        user.user_name = self.user_name.lower()
        user.password = self.password
        user.edit()
        return "Done"
