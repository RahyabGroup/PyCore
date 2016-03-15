from bson import ObjectId
from pyfacil.reposiotry.mongo.gridfs.repository import Repository
from pystatic.main.config import Config

__author__ = 'Hooman'


class FileWriter(Repository):
    def __init__(self, storage_name):
        cfg = Config()
        super(FileWriter, self).__init__(cfg.mongo_connection, storage_name)

    def create(self, file):
        if not file._id:
            file._id = str(ObjectId())

        self.collection.writer.add(file.content, original_file_name=file.original_file_name, path=file.path,
                                   persisted_file_name=file.persisted_file_name, storage_name=file.storage_name,
                                   _id=ObjectId(file._id))

    def remove_by_path(self, path):
        self.collection.writer.remove_by_condition({"path": path})
