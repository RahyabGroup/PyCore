from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.apk.app.v1_0.rest.resource import *
from pystatic.domain.aggregates.apk.model.validation.apk_file_extension_not_exist import ApkFileExtensionNotExist
from pystatic.domain.aggregates.apk.model.validation.apk_file_name_exist import ApkFileNameExist
from pystatic.domain.aggregates.apk.model.validation.apk_version_id_exist import ApkVersionIdExist

__author__ = 'H.Rouhani'


class ApkUploadValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.storage_name, 2, 20)
        super().string.size(self.instance.file["file_name"], 2, 500)
        super().string.size(self.instance.package_name, 2, 150)
        super().string.size(self.instance.version, 2, 50)
        super().integer.positive(self.instance.version_id, include_zero=False)
        super().validate()
        if not self.instance.file["file_content"]:
            super().custom.manual(ApkErrorCodes.RESOURCE_CONTENT_IS_EMPTY)
        if not file_info.get_file_name(self.instance.file["file_name"]) or not file_info.get_extension(
                self.instance.file["file_name"]):
            super().custom.manual(ApkErrorCodes.APK_NAME_OR_EXTENSION_NOT_EXIST, data=self.instance.file["file_name"])

        super().custom.register(self.instance.file["file_name"], ApkFileExtensionNotExist())
        super().custom.register("{}_{}.{}".format(self.instance.package_name, self.instance.version,
                                                  file_info.get_extension(self.instance.file["file_name"])),
                                ApkFileNameExist(self.instance.storage_name))
        super().custom.register(self.instance.version_id, ApkVersionIdExist(self.instance.storage_name))
        super().validate()
