

__author__ = 'Hooman'


class UserRemovedToken:
    user_id = None

    def __init__(self, dto):
        self.user_id = dto["user_id"]

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        Token.remove_by_user_id(self.user_id)
