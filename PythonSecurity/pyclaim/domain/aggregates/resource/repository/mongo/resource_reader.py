from bson import ObjectId
from pyfacil.reposiotry.mongo.searcher import Searcher
from pyclaim.main.config import Config

__author__ = 'Hooman'


class ResourceReader(Searcher):
    def __init__(self):
        cfg = Config()
        super(ResourceReader, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "resource")

    def get_main_info(self, id):
        return self._collection.reader.find_one({"_id": ObjectId(id)}, fields=["_id", "name"])

    def exist_name(self, name):
        return self._collection.reader.is_available({"name": name})

    def get_by_name(self, name):
        return self._collection.reader.find_one({"name": name})

    def get_all(self):
        return self._collection.reader.find_many({}, sort={"name": 1})

    def claim_exist(self, resource_id, claim_type_id, claim_value):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(resource_id)},
                                                             {"claims.claim_type._id": claim_type_id},
                                                             {"claims.value": claim_value}]})

    def claim_id_exist(self, resource_id, claim_id):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(resource_id)},
                                                             {"claims._id": claim_id}]})

    def claim_is_of_claim_type(self, resource_id, claim_id, claim_type_id):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(resource_id)},
                                                             {"claims.claim_type._id": claim_type_id},
                                                             {"claims._id": claim_id}]})
