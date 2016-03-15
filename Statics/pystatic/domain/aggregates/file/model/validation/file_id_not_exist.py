from pyvalidate.validation import Validation
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileErrorCodes
from pystatic.domain.aggregates.file.model.file import File

__author__ = 'H.Rouhani'


class FileIdNotExist(Validation):
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def validate(self, file_id):
        file_exist = File.id_exists(self.storage_name, file_id)
        if not file_exist:
            super().custom.manual(FileErrorCodes.FILE_ID_NOT_EXIST, data=file_id)
