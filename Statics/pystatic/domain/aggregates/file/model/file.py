from bson import ObjectId
from pyutil.file import file_info
from pystatic.domain.aggregates.file.app.v1_0.rest.assembler import *


__author__ = 'H.Rouhani'


class File:
    _id = None
    content = None
    original_file_name = None
    persisted_file_name = None
    path = None

    def __init__(self, storage_name):
        self.storage_name = storage_name

    @staticmethod
    def path_exist(storage_name, path):
        return file_reader(storage_name).path_exist(path)

    @staticmethod
    def get_by_id(storage_name, file_id):
        return file_reader(storage_name).get_by_id(file_id)

    @staticmethod
    def id_exists(storage_name, file_id):
        return file_reader(storage_name).exist_id(file_id)

    def create(self):
        self._id = str(ObjectId())
        self._persisted_file_name_create()
        self._path_create()
        file_writer(self.storage_name).create(self)

    def replace(self):
        self._path_create()
        file_writer(self.storage_name).remove_by_path(self.path)
        file_writer(self.storage_name).create(self)

    def remove_by_path(self):
        file_writer(self.storage_name).remove_by_path(self.path)

    def _persisted_file_name_create(self):
        self.persisted_file_name = "{}.{}".format(self._id, file_info.get_extension(self.original_file_name))

    def _path_create(self):
        self.path = "/files/{}/{}".format(self.storage_name, self.persisted_file_name)
