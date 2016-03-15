
__author__ = 'H.Rouhani'


class RequestTokenRemove:
    token_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token

        Token.remove(self.token_id)
