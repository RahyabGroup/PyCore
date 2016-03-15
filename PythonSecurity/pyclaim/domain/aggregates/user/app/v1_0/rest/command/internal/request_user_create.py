from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class RequestUserCreate:
    user_name = None
    password = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user.user_name = self.user_name.lower()
        user.password = self.password
        user.create()
        return "Done"
