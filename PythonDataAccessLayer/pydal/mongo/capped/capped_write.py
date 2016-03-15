from datetime import datetime
from bson import ObjectId
from pyutil.serialization.json.date_time_bson_serialize_handler import DatetimeBsonSerializeHandler
from pyutil.serialization.json.object_id_bson_serialize_handler import ObjectIdBsonSerializeHandler
from pyutil.serialization.json.serializer import Serializer

__author__ = 'Hooman'


class CappedWriteCommand:
    def __init__(self, mongo_collection):
        self._mongo_collection = mongo_collection

    def save(self, data):
        serialized_data_dictionary = self._get_document(data)
        self._mongo_collection.save(serialized_data_dictionary)

    def add(self, data):
        serialized_data_dictionary = self._get_document(data)
        self._mongo_collection.insert(serialized_data_dictionary)

    def edit(self, data):
        serialized_data_dictionary = self._get_document(data)
        self._mongo_collection.update({"_id": serialized_data_dictionary["_id"]}, serialized_data_dictionary)

    def edit_by_condition(self, first_query, second_query, multi=True):
        self._mongo_collection.update(first_query, second_query, multi=multi)

    def _get_document(self, data):
        if not hasattr(data, "_id") or not data._id:
            data._id = ObjectId()
        elif isinstance(data._id, str):
            data._id = ObjectId(data._id)
        json_serializer = Serializer()
        json_serializer.add_handler(datetime, DatetimeBsonSerializeHandler)
        json_serializer.add_handler(ObjectId, ObjectIdBsonSerializeHandler)
        document = json_serializer.serialize_to_dictionary(data)
        data._id = str(data._id)
        return document