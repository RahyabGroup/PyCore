from pyutil.file import file_info

from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.validation.file_replace_validator import FileReplaceValidator
from pystatic.domain.aggregates.file.model.file import File
from pystatic.main.assembler import validator

__author__ = 'root'


@validator.validation(FileReplaceValidator)
class FileReplace:
    storage_name = None
    old_file_name = None
    new_file = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file_id = file_info.get_file_name(self.old_file_name)
        file = File(self.storage_name)
        file._id = file_id
        file.persisted_file_name = self.old_file_name
        file.original_file_name = self.new_file["file_name"]
        file.content = self.new_file["file_content"]
        file.replace()