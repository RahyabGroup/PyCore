
__author__ = 'Hooman'


class RequestTokenAuthenticated:
    token_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        return Token.exist(self.token_id)
