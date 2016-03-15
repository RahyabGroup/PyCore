from pystatic.domain.aggregates.apk.app.v1_0.rest.query.public.validation.apk_download_by_version_id_validator import ApkDownloadByVersionIdValidator
from pystatic.domain.aggregates.apk.app.v1_0.rest.view_model.detail.apk_download_detail import ApkDownloadDetail
from pystatic.domain.aggregates.apk.model.apk import Apk
from pystatic.main.assembler import validator

__author__ = 'root'


@validator.validation(ApkDownloadByVersionIdValidator)
class ApkDownloadByVersionId:
    storage_name = None
    version_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        apk = Apk.get_by_version_id(self.storage_name, self.version_id)
        return ApkDownloadDetail.create_from_apk(apk)
