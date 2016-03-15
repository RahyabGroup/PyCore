from bson import ObjectId
from pyfacil.reposiotry.mongo.repository import Repository
from pyutil.serialization.json.serializer import Serializer
from pyclaim.main.config import Config

__author__ = 'Hooman'


class ResourceWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(ResourceWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "resource")

    def claim_remove_by_claim_type(self, claim_type_id):
        self._collection.writer.edit_by_condition({},
                                                 {"$pull": {"claims": {"claim_type_id": str(claim_type_id)}}})

    def edit_main_info(self, resource):
        self._collection.writer.edit_by_condition({"_id": ObjectId(resource._id)}, {"$set": {"name": resource.name}})

    def claim_add(self, resource_id, claim):
        serializer = Serializer()
        claim_dict = serializer.serialize_to_dictionary(claim)
        self._collection.writer.edit_by_condition({"_id": ObjectId(resource_id)},
                                                 {"$push": {"claims": claim_dict}})

    def claim_edit(self, resource_id, claim):
        serializer = Serializer()
        claim_dict = serializer.serialize_to_dictionary(claim)
        self._collection.writer.edit_by_condition({"_id": ObjectId(resource_id), "claims._id": claim._id},
                                                 {"$set": {"claims.$": claim_dict}})

    def claim_remove(self, resource_id, claim_id):
        self._collection.writer.edit_by_condition({"_id": ObjectId(resource_id)},
                                                 {"$pull": {"claims": {"_id": claim_id}}})

