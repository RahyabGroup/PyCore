from pyfacil.reposiotry.mongo.searcher import Searcher
from pyclaim.main.config import Config

__author__ = 'Hooman'


class ClaimTypeReader(Searcher):
    def __init__(self):
        cfg = Config()
        super(ClaimTypeReader, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "claim_type")

    def exist_name(self, name):
        return self._collection.reader.is_available({"name": name})

    def get_by_name(self, name):
        return self._collection.reader.find_one({"name": name})

    def get_all(self):
        return self._collection.reader.find_many({}, sort={"name": 1})
