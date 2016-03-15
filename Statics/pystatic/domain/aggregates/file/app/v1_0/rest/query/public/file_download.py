from pyutil.file import file_info

from pystatic.domain.aggregates.file.app.v1_0.rest.query.public.validation.file_download_validator import FileDownloadValidator
from pystatic.domain.aggregates.file.app.v1_0.rest.view_model.detail.file_download_detail import FileDownloadDetail
from pystatic.domain.aggregates.file.model.file import File
from pystatic.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(FileDownloadValidator)
class FileDownload:
    storage_name = None
    file_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        file_id = file_info.get_file_name(self.file_name)
        file = File.get_by_id(self.storage_name, file_id)
        return FileDownloadDetail.create_from_file(file)
