__author__ = 'H.Rouhani'


class TokenDetail:
    _id = None
    token_id = None
    user_id = None
    login_type = None

    @staticmethod
    def create_from_token(token):
        if token:
            token_detail = TokenDetail()
            token_detail._id = token._id
            token_detail.user_id = token.user_id
            token_detail.login_type = token.login_type
            token_detail.token_id = token.token_id
            return token_detail
        return None
