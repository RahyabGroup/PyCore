from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.validation.file_remove_validator import \
    FileRemoveValidator
from pystatic.domain.aggregates.file.model.file import File
from pystatic.main.assembler import validator

__author__ = 'root'


@validator.validation(FileRemoveValidator)
class FileRemove:
    storage_name = None
    file_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file = File(self.storage_name)
        file.persisted_file_name = self.file_name
        file.remove_by_path()
