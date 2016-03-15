from bson import ObjectId
from pyclaim.domain.aggregates.token.app.v1_0.rest.assembler import token_reader, token_writer

__author__ = 'Hooman'


class Token:
    _id = None
    token_id = None
    user_id = None
    login_type = None

    def __init__(self, user_id, token_id):
        self.user_id = user_id
        self.token_id = token_id
        self._id = token_id

    @staticmethod
    def get_by_id(token_id):
        return token_reader.get_by_id(token_id)

    @staticmethod
    def exist(token_id):
        return token_reader.exist(token_id)

    @staticmethod
    def generate(user_id):
        token_id = str(ObjectId())
        user_token = Token(user_id, token_id)
        token_writer.create(user_token)
        return user_token

    @staticmethod
    def remove(token_id):
        token_writer.remove(token_id)

    @staticmethod
    def remove_by_user_id(user_id):
        token_writer.remove_by_user_id(user_id)