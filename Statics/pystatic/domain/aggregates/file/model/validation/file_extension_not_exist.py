from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileErrorCodes

from pystatic.domain.aggregates.file.model.file_extentions import FileExtentions

__author__ = 'H.Rouhani'


class FileExtensionNotExist(Validation):
    def validate(self, original_file_name):
        file_extension = file_info.get_extension(original_file_name)

        if not file_extension.strip().lower() in FileExtentions.FILE_EXTENTIONS:
            super().custom.manual(FileErrorCodes.FILE_EXTENSION_IS_NOT_VALID, data=file_extension)
