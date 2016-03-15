from pyfacil.reposiotry.mongo.gridfs.searcher import Searcher
from pystatic.main.config import Config

__author__ = 'H.Rouhani'


class ApkReader(Searcher):
    def __init__(self, storage_name):
        cfg = Config()
        super(ApkReader, self).__init__(cfg.mongo_connection, storage_name)

    def file_name_exist(self, file_name):
        return self._collection.reader.is_available({"persisted_file_name": file_name})

    def get_by_file_name(self, file_name):
        result = self._collection.reader.find_one({"persisted_file_name": file_name})
        return self._get_apk_instance(result)

    def get_by_version_id(self, version_id):
        result = self._collection.reader.find_one({"version.version_id": version_id})
        return self._get_apk_instance(result)

    def version_id_exist(self, version_id):
        return self._collection.reader.is_available({"version.version_id": version_id})

    def get_all(self, skip, take):
        results = self._collection.reader.find_many({}, skip=skip, take=take)
        apks = []
        for result in results:
            apks.append(self._get_apk_instance(result))
        return apks

    def _get_apk_instance(self, result):
        from pystatic.domain.aggregates.apk.model.apk import Apk
        from pystatic.domain.aggregates.apk.model.version import Version
        apk = Apk(result["info"]["storage_name"])
        apk.content = result["binary_data"]
        apk._id = str(result["info"]["_id"])
        apk.upload_date = result["info"]["upload_date"]
        apk.package_name = result["info"]["package_name"]
        apk.version = Version()
        apk.version.version_id = result["info"]["version"]["version_id"]
        apk.version.version_name = result["info"]["version"]["version_name"]
        apk.original_file_name = result["info"]["original_file_name"]
        apk.persisted_file_name = result["info"]["persisted_file_name"]
        apk.path = result["info"]["path"]
        return apk
