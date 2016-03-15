from pydal.mongo.connection import Connection

__author__ = 'H.Rouhani'


class Repository:
    def __init__(self, connection_string, db_name):
        self._connection = Connection(connection_string)
        self._db = self._connection.gridfsdb(db_name)
        self.collection = self._db.gridfs_collection()
