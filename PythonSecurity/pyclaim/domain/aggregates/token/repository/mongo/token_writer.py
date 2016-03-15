from pyfacil.reposiotry.mongo.repository import Repository
from pyclaim.main.config import Config

__author__ = 'Hooman'


class TokenWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(TokenWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "token")

    def remove_by_user_id(self, user_id):
        return self._collection.writer.remove_by_condition({"user_id": user_id})

    def remove(self, token_id):
        return self._collection.writer.remove_by_condition({"token_id": token_id})

    def remove_all(self):
        return self._collection.writer.remove_all()
