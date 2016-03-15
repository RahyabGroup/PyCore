from pyvalidate.validation import Validation
from pystatic.domain.aggregates.apk.app.v1_0.rest.resource import ApkErrorCodes
from pystatic.domain.aggregates.apk.model.apk import Apk

__author__ = 'root'


class ApkVersionIdExist(Validation):
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def validate(self, version_id):
        file_version_id_exist = Apk.version_id_exist(self.storage_name, version_id)
        if file_version_id_exist:
            super().custom.manual(ApkErrorCodes.APK_VERSION_ID_EXIST)
