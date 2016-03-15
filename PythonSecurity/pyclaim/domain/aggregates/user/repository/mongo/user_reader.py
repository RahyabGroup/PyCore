from bson import ObjectId
from pyfacil.reposiotry.mongo.searcher import Searcher

from pyclaim.main.config import Config

__author__ = 'Hooman'


class UserReader(Searcher):
    def __init__(self):
        cfg = Config()
        super(UserReader, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "user")

    def get_by_user_name(self, user_name):
        return self._collection.reader.find_one({"user_name": user_name})

    def password_get_by_user_name(self, user_name):
        user = self._collection.reader.find_one({"user_name": user_name}, fields=["password"])
        return user.password

    def exist_with_user_name(self, user_name):
        return self._collection.reader.is_available({"user_name": user_name})

    def password_exist(self, user_id, password):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(user_id)}, {"password": password}]})

    def get_by_user_name_and_password(self, user_name, password):
        return self._collection.reader.find_one({"$and": [{"user_name": user_name}, {"password": password}]})

    def get_all(self):
        return self._collection.reader.find_many({}, sort={"user_name": 1})

    def get_main_info(self, user_id):
        return self._collection.reader.find_one({"_id": ObjectId(user_id)}, fields=["_id", "user_name", "password"])

    def user_name_get_by_id(self, user_id):
        user = self._collection.reader.find_one({"_id": ObjectId(user_id)}, fields=["user_name"])
        return user.user_name

    def claim_exist(self, user_id, claim_type_id, claim_value):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(user_id)},
                                                              {"claims.claim_type._id": claim_type_id},
                                                              {"claims.value": claim_value}]})

    def claim_id_exist(self, user_id, claim_id):
        return self._collection.reader.is_available({"$and": [{"_id": ObjectId(user_id)},
                                                              {"claims._id": claim_id}]})

    def claims_get_claim_type_id(self, user_id, claim_type_id):
        search_query_currently_work_here = [{"$unwind": "$claims"},
                                            {"$match": {"$and":
                                                            [{"_id": ObjectId(user_id)},
                                                             {"claims.claim_type._id": claim_type_id}]}}]

        users = self._collection.reader.aggregate(fields=["claims"], query=search_query_currently_work_here)

        result = []
        if users:
            for user in users:
                if user.claims:
                    result.append(user.claims)
        return result