from pystatic.domain.aggregates.apk.app.v1_0.rest.command.public.validation.apk_upload_validator import ApkUploadValidator
from pystatic.domain.aggregates.apk.app.v1_0.rest.view_model.detail.apk_upload_detail import ApkUploadDetail
from pystatic.domain.aggregates.apk.model.apk import Apk
from pystatic.domain.aggregates.apk.model.version import Version
from pystatic.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(ApkUploadValidator)
class ApkUpload:
    package_name = None
    version = None
    version_id = None
    storage_name = None
    file = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        apk = Apk(self.storage_name)
        apk.package_name = self.package_name
        version = Version()
        version.version_name = self.version
        version.version_id = self.version_id
        apk.version_set(version)
        apk.content = self.file["file_content"]
        apk.original_file_name = self.file["file_name"]
        apk.create()
        return ApkUploadDetail.create_from_apk(apk)
