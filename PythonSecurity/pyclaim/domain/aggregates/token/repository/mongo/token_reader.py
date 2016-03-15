from pyfacil.reposiotry.mongo.searcher import Searcher
from pyclaim.main.config import Config

__author__ = 'Hooman'


class TokenReader(Searcher):
    def __init__(self):
        cfg = Config()
        super(TokenReader, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "token")

    def exist(self, token_id):
        return self._collection.reader.is_available({"token_id": token_id})
