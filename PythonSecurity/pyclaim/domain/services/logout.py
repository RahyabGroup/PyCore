from pyutil.cryptography.rsa.object_coder import ObjectCoder

from pyclaim.main.config import Config


__author__ = 'H.Rouhani'


class Logout:
    token = None

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        decrypted_token = ObjectCoder(Config().secret_key).decode(self.token)
        token_id = decrypted_token["token_id"]
        Token.remove(token_id)
        return "Done"
