from bson import ObjectId
from pydal.mongo.connection import Connection

__author__ = 'H.Rouhani'


class Searcher:
    def __init__(self, connection_string, db_name):
        self._connection = Connection(connection_string)
        self._db = self._connection.gridfsdb(db_name)
        self._collection = self._db.gridfs_collection()

    def exist_id(self, id):
        return self._collection.reader.is_available_id(ObjectId(id))

    def exist_id_async(self, id):
        return (yield from self._collection.reader.is_available_id(ObjectId(id)))
