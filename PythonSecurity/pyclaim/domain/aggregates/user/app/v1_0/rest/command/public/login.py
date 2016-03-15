from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.login_container import LoginContainer
from pyclaim.main.assembler import validator
from pyclaim.domain.services.login import Login as LoginService
__author__ = 'Hooman'


@validator.validation(LoginContainer)
class Login:
    user_name = None
    password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        login_service = LoginService()
        login_service.user_name = self.user_name.lower()
        login_service.password = self.password
        return login_service.execute()
