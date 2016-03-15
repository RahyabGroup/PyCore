from pydal.mongo.connection import Connection

__author__ = 'H.Rouhani'


class Repository:
    def __init__(self, connection_string, db_name, collection, is_capped_collection=False):
        self._connection = Connection(connection_string)
        self._db = self._connection.db(db_name)

        if is_capped_collection:
            self._collection = self._db.capped_collection(collection)
        else:
            self._collection = self._db.collection(collection)

    def create(self, item):
        self._collection.writer.add(item)

    def create_async(self, item):
        yield from self._collection.async_writer.add(item)

    def delete(self, id):
        self._collection.writer.remove_by_id(id)

    def delete_async(self, id):
        yield from self._collection.async_writer.remove_by_id(id)

    def update(self, item):
        self._collection.writer.edit(item)

    def update_async(self, item):
        yield from self._collection.async_writer.edit(item)
