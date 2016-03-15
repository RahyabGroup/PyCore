from pyutil.file import file_info
from pyvalidate.validation import Validation
from pystatic.domain.aggregates.apk.app.v1_0.rest.resource import ApkErrorCodes

__author__ = 'H.Rouhani'


class ApkFileExtensionNotExist(Validation):
    def validate(self, file_name):
        file_extension = file_info.get_extension(file_name)

        if not file_extension.strip().lower() in ['apk']:
            super().custom.manual(ApkErrorCodes.APK_EXTENSION_IS_NOT_VALID, data=file_extension)
