from bson import ObjectId
from pyfacil.reposiotry.mongo.gridfs.repository import Repository
from pystatic.main.config import Config

__author__ = 'H.Rouhani'


class ApkWriter(Repository):
    def __init__(self, storage_name):
        cfg = Config()
        super(ApkWriter, self).__init__(cfg.mongo_connection, storage_name)

    def create(self, apk):
        if not apk._id:
            apk._id = str(ObjectId())

        self.collection.writer.add(apk.content, upload_date=apk.upload_date, persisted_file_name=apk.persisted_file_name,
                                   package_name=apk.package_name, original_file_name=apk.original_file_name,
                                   version={"version_name": apk.version.version_name,
                                            "version_id": apk.version.version_id},
                                   path=apk.path, storage_name=apk.storage_name, _id=ObjectId(apk._id))
