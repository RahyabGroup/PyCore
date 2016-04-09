from pyutil.file import file_info
from pyvalidate.validation import Validation

from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.validation.file_name_is_invalid import FileNameIsInvalid
from pystatic.domain.aggregates.file.app.v1_0.rest.resource import FileErrorCodes
from pystatic.domain.aggregates.file.model.validation.file_extension_not_exist import FileExtensionNotExist
from pystatic.domain.aggregates.file.model.validation.file_id_not_exist import FileIdNotExist

__author__ = 'root'


class FileReplaceValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.old_file_name, 2, 500)
        super().string.size(self.instance.storage_name, 2, 20)
        super().string.size(self.instance.new_file["file_name"], 2, 500)
        super().validate()
        if not self.instance.new_file["file_content"]:
            super().custom.manual(FileErrorCodes.RESOURCE_CONTENT_IS_EMPTY)
        super().custom.register(self.instance.old_file_name, FileNameIsInvalid())
        super().custom.register(self.instance.new_file["file_name"], FileNameIsInvalid())
        super().validate()
        file_id = file_info.get_file_name(self.instance.old_file_name)
        super().custom.register(file_id, FileIdNotExist(self.instance.storage_name))
        super().validate()