from pystatic.domain.aggregates.apk.app.v1_0.rest.query.public.validation.apk_download_validator import ApkDownloadValidator
from pystatic.domain.aggregates.apk.app.v1_0.rest.view_model.detail.apk_download_detail import ApkDownloadDetail
from pystatic.domain.aggregates.apk.model.apk import Apk
from pystatic.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(ApkDownloadValidator)
class ApkDownload:
    storage_name = None
    file_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        apk = Apk.get_by_file_name(self.storage_name, self.file_name)
        return ApkDownloadDetail.create_from_apk(apk)

