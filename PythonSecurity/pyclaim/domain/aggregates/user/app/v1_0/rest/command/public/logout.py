from pyclaim.domain.services.logout import Logout as LogoutService
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.logout_container import LogoutContainer
from pyclaim.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(LogoutContainer)
class Logout:
    token = None

    def __init__(self, token_string):
        self.token = token_string

    def execute(self):
        logout_service = LogoutService()
        logout_service.token = self.token
        return logout_service.execute()
