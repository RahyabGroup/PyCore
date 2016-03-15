from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileErrorCodes

__author__ = 'root'


class FileNameIsInvalid(Validation):
    def validate(self, file_name):
        if "." not in file_name:
            super().custom.manual(FileErrorCodes.FILE_NAME_IS_INVALID, data=file_name)
        else:
            if not file_info.get_file_name(file_name) or not file_info.get_extension(file_name):
                super().custom.manual(FileErrorCodes.FILE_NAME_OR_EXTENSION_NOT_EXIST, file_name)


