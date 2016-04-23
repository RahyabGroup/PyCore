from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.file.app.v1_0.rest.command.public.validation.file_name_is_invalid import FileNameIsInvalid
from pystatic.domain.aggregates.file.model.validation.file_id_not_exist import FileIdNotExist

__author__ = 'root'


class FileRemoveValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.file_name, 2, 500)
        super().string.size(self.instance.storage_name, 2, 20)
        super().validate()
        super().custom.register(self.instance.file_name, FileNameIsInvalid())
        super().validate()
        file_id = file_info.get_file_name(self.instance.file_name)
        super().custom.register(file_id, FileIdNotExist(self.instance.storage_name))
        super().validate()