from pymongo.mongo_client import MongoClient

from pydal.mongo.db import Db
from pydal.mongo.gridfs.gridfs_db import GridfsDb

__author__ = 'Hooman'


class Connection:
    def __init__(self, connection_string):
        self._connection_string = connection_string
        self._mongo_connection = MongoClient(connection_string)

    def db(self, name):
        mongodb = self._mongo_connection[name]
        db = Db(name, mongodb)
        return db

    def gridfsdb(self, name):
        mongodb = self._mongo_connection[name]
        gridfs_db = GridfsDb(mongodb)
        return gridfs_db

