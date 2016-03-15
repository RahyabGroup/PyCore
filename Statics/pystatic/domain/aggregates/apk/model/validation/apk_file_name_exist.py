from pyvalidate.validation import Validation
from pystatic.domain.aggregates.apk.app.v1_0.rest.resource import ApkErrorCodes

from pystatic.domain.aggregates.apk.model.apk import Apk

__author__ = 'H.Rouhani'


class ApkFileNameExist(Validation):
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def validate(self, file_name):
        file_name_exist = Apk.file_name_exist(self.storage_name, file_name)
        if file_name_exist:
            super().custom.manual(ApkErrorCodes.APK_FILE_NAME_EXIST)
