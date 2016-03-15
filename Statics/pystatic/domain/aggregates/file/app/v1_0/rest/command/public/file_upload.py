from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.validation.file_upload_validator import FileUploadValidator
from pystatic.domain.aggregates.file.app.v1_0.rest.view_model.detail.file_upload_detail import FileUploadDetail
from pystatic.domain.aggregates.file.model.file import File
from pystatic.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(FileUploadValidator)
class FileUpload:
    storage_name = None
    file = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file = File(self.storage_name)
        file.original_file_name = self.file["file_name"]
        file.content = self.file["file_content"]
        file.create()
        return FileUploadDetail.create_from_file(file)
