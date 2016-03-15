from datetime import datetime

from pyutil.file import file_info
from pystatic.domain.aggregates.apk.app.v1_0.rest.assembler import apk_writer, apk_reader

__author__ = 'H.Rouhani'


class Apk:
    _id = None
    upload_date = None
    package_name = None
    version = None
    content = None
    original_file_name = None
    persisted_file_name = None
    path = None

    def __init__(self, storage_name):
        self.storage_name = storage_name

    @staticmethod
    def file_name_exists(storage_name, file_name):
        return apk_reader(storage_name).file_name_exist(file_name)

    @staticmethod
    def get_by_file_name(storage_name, file_name):
        return apk_reader(storage_name).get_by_file_name(file_name)

    @staticmethod
    def get_by_version_id(storage_name, version_id):
        return apk_reader(storage_name).get_by_version_id(version_id)

    @staticmethod
    def get_all(storage_name, skip, take):
        return apk_reader(storage_name).get_all(skip, take)

    @staticmethod
    def version_id_exist(storage_name, version_id):
        return apk_reader(storage_name).version_id_exist(version_id)

    @staticmethod
    def file_name_exist(storage_name, file_name):
        return apk_reader(storage_name).file_name_exist(file_name)

    def create(self):
        self.persisted_file_name = self._persisted_file_name_get()
        self.path = self._path_get()
        self.upload_date = datetime.utcnow()
        apk_writer(self.storage_name).create(self)

    def version_set(self, version):
        self.version = version

    def _path_get(self):
        return "/apks/{}/{}".format(self.storage_name, self.persisted_file_name)

    def _persisted_file_name_get(self):
        return "{}_{}.{}".format(self.package_name, self.version.version_name,
                                 file_info.get_extension(self.original_file_name))
