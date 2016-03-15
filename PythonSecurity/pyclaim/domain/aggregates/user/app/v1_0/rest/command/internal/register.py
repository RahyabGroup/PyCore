from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.validation.register_container import \
    RegisterContainer
from pyclaim.main.assembler import validator

__author__ = 'root'


@validator.validation(RegisterContainer)
class Register:
    user_name = None
    password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        from pyclaim.domain.services.register import Register as RegisterService

        register_service = RegisterService()
        register_service.user_name = self.user_name.lower()
        register_service.password = self.password
        result = register_service.execute()
        return result
