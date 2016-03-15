from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.validation.password_change_container import \
    PasswordChangeContainer
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(PasswordChangeContainer)
class PasswordChange:
    user_id = None
    old_password = None
    new_password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = self.user_id
        user.password = self.old_password
        user.password_change(self.new_password)
