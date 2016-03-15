from pyclaim.domain.aggregates.token.app.v1_0.rest.view_model.detail.token import TokenDetail


__author__ = 'H.Rouhani'


class RequestTokenGetById:
    token_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        token = Token.get_by_id(self.token_id)
        token_detail = None
        if token:
            token_detail = TokenDetail.create_from_token(token)
        return token_detail
