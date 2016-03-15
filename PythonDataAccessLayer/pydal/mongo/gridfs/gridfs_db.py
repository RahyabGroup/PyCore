from gridfs import GridFS

from pydal.mongo.gridfs.gridfs_collection import GridfsCollection

__author__ = 'Hooman'


class GridfsDb:
    def __init__(self, mongodb):
        self._mongodb = mongodb

    def gridfs_collection(self):
        fs = GridFS(self._mongodb)
        gridfs_collection = GridfsCollection(fs)
        return gridfs_collection
