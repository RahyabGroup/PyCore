from bson import ObjectId
from pydal.mongo.connection import Connection

__author__ = 'H.Rouhani'


class Searcher:
    def __init__(self, connection_string, db_name, collection, is_capped_collection=False):
        self._connection = Connection(connection_string)
        self._db = self._connection.db(db_name)

        if is_capped_collection:
            self._collection = self._db.capped_collection(collection)
        else:
            self._collection = self._db.collection(collection)

    def get_by_id(self, id):
        return self._collection.reader.find_one({"_id": ObjectId(id)})

    def get_by_id_async(self, id):
        return (yield from self._collection.async_reader.find_one({"_id": ObjectId(id)}))

    def count(self):
        return self._collection.reader.count()

    def count_async(self):
        return self._collection.async_reader.count()

    def exist_id(self, id):
        return self._collection.reader.is_available({"_id": ObjectId(id)})

    def exist_id_async(self, id):
        return (yield from self._collection.async_reader.is_available({"_id": ObjectId(id)}))
