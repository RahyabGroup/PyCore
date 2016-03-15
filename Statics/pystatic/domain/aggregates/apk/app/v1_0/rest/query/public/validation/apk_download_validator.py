from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.apk.app.v1_0.rest.resource import ApkErrorCodes

from pystatic.domain.aggregates.apk.model.validation.apk_file_name_not_exist import ApkFileNameNotExist

__author__ = 'H.Rouhani'


class ApkDownloadValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.file_name, 3, 100)
        super().string.size(self.instance.storage_name, 2, 20)
        super().validate()
        if not file_info.get_file_name(self.instance.file_name):
            super().custom.manual(ApkErrorCodes.APK_NAME_OR_EXTENSION_NOT_EXIST)
        super().custom.register(self.instance.file_name, ApkFileNameNotExist(self.instance.storage_name))
        super().validate()
