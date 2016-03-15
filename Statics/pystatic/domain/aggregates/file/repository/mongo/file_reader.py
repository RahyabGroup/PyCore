from bson import ObjectId
from pyfacil.reposiotry.mongo.gridfs.searcher import Searcher
from pystatic.main.config import Config

__author__ = 'Hooman'


class FileReader(Searcher):
    def __init__(self, storage_name):
        cfg = Config()
        super(FileReader, self).__init__(cfg.mongo_connection, storage_name)

    def get_by_id(self, id):
        from pystatic.domain.aggregates.file.model.file import File
        result = self._collection.reader.get(ObjectId(id))
        file = File(result["info"]["storage_name"])
        file._id = str(result["info"]["_id"])
        file.content = result["binary_data"]
        file.original_file_name = result["info"]["original_file_name"]
        file.persisted_file_name = result["info"]["persisted_file_name"]
        file.path = result["info"]["path"]
        return file

    def path_exist(self, path):
        return self._collection.reader.is_available({"path": path})
