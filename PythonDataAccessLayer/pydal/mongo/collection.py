from pydal.mongo.async_read import AsyncReadCommand
from pydal.mongo.async_write import AsyncWriteCommand
from pydal.mongo.read import ReadCommand
from pydal.mongo.write import WriteCommand

__author__ = 'Hooman'


class Collection:
    def __init__(self, collection_name, mongo_collection):
        self.collection_name = collection_name
        self._mongo_collection = mongo_collection

    def create_index(self, index):
        self._mongo_collection.create_index(index)

    def _get_reader(self):
        pydal_reader = ReadCommand(self._mongo_collection)
        return pydal_reader

    def _get_writer(self):
        pydal_writer = WriteCommand(self._mongo_collection)
        return pydal_writer

    def _get_async_reader(self):
        pydal_reader = AsyncReadCommand(self._mongo_collection)
        return pydal_reader

    def _get_async_writer(self):
        pydal_writer = AsyncWriteCommand(self._mongo_collection)
        return pydal_writer

    reader = property(_get_reader)
    writer = property(_get_writer)
    async_reader = property(_get_async_reader)
    async_writer = property(_get_async_writer)
