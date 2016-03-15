from pydal.mongo.gridfs.gridfs_read import GridfsRead
from pydal.mongo.gridfs.async_gridfs_read import AsyncGridfsRead
from pydal.mongo.gridfs.async_gridfs_write import AsyncGridfsWrite

from pydal.mongo.gridfs.gridfs_write import GridfsWrite

__author__ = 'H.Rouhani'


class GridfsCollection:
    def __init__(self, fs):
        self._fs = fs

    def _get_reader(self):
        gridfs_reader = GridfsRead(self._fs)
        return gridfs_reader

    def _get_writer(self):
        gridfs_writer = GridfsWrite(self._fs)
        return gridfs_writer

    def _get_async_reader(self):
        gridfs_reader = AsyncGridfsRead(self._fs)
        return gridfs_reader

    def _get_async_writer(self):
        gridfs_writer = AsyncGridfsWrite(self._fs)
        return gridfs_writer

    reader = property(_get_reader)
    writer = property(_get_writer)
    async_reader = property(_get_async_reader)
    async_writer = property(_get_async_writer)
