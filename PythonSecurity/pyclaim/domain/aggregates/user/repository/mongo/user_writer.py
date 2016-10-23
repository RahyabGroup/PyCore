from bson import ObjectId
from pyfacil.reposiotry.mongo.repository import Repository
from pyutil.serialization.json.serializer import Serializer

from pyclaim.main.config import Config

__author__ = 'Hooman'


class UserWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(UserWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "user")

    def claim_remove_by_claim_type(self, claim_type_id):
        self._collection.writer.edit_by_condition({},
                                                  {"$pull": {"claims": {"claim_type_id": str(claim_type_id)}}})

    def claim_remove_by_value(self, value):
        self._collection.writer.edit_by_condition({}, {"$pull": {"claims": {"value": value}}})

    def claim_update_value_by_new_value(self, old_value, new_value):
        self._collection.writer.edit_by_condition({"claims.value": old_value},
                                                  {"$set": {"claims.$.value": new_value}})

    def edit_main_info(self, user):
        self._collection.writer.edit_by_condition({"_id": ObjectId(user._id)},
                                                  {"$set": {"user_name": user.user_name,
                                                            "password": user.password}})

    def claim_add(self, user_id, claim):
        serializer = Serializer()
        claim_dict = serializer.serialize_to_dictionary(claim)
        self._collection.writer.edit_by_condition({"_id": ObjectId(user_id)},
                                                  {"$push": {"claims": claim_dict}})

    def claim_edit(self, user_id, claim):
        serializer = Serializer()
        claim_dict = serializer.serialize_to_dictionary(claim)
        self._collection.writer.edit_by_condition({"$and": {"_id": ObjectId(user_id), "claims._id": claim._id}},
                                                  {"$set": {"claims.$": claim_dict}})

    def claim_remove(self, user_id, claim_id):
        self._collection.writer.edit_by_condition({"_id": ObjectId(user_id)},
                                                  {"$pull": {"claims": {"_id": claim_id}}})

    def claim_remove_by_claim_type_name_with_value(self, user_id, claim_type_id, claim_value):
        return self._collection.writer.edit_by_condition({"_id": ObjectId(user_id)},
                                                         {"$pull":
                                                             {"claims":
                                                                 {"$and": [
                                                                     {"claim_type_id": claim_type_id},
                                                                     {"value": claim_value}]}}})

    def claim_edit_by_claim_type_name_with_value(self, user_id, claim_type_id, claim_old_value, claim_value):
        self._collection.writer.edit_by_condition({"$and": {"_id": ObjectId(user_id),
                                                            "claims.claim_type_id": claim_type_id,
                                                            "claims.value": claim_old_value}},
                                                  {"$set": {"claims.$.value": claim_value}})

    def password_change(self, user_id, new_password):
        serializer = Serializer()
        password_dict = serializer.serialize_to_dictionary(new_password)
        self._collection.writer.edit_by_condition({"_id": ObjectId(user_id)},
                                                  {"$set": {"password": password_dict}})

    def change_status(self, user_id, status):
        self._collection.writer.edit_by_condition({"_id": ObjectId(user_id)},
                                                  {"$set": {"status": status}})
