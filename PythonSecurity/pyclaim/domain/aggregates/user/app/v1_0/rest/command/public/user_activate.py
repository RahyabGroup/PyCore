from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_activate_container import \
    UserActivateContainer
from pyclaim.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(UserActivateContainer)
class UserActivate:
    user_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        from pyclaim.domain.aggregates.user.model.user import User

        user = User()
        user._id = self.user_id
        user.activate()
