from pyfacil.web.query_string.query_string_info import QueryStringInfo
from pystatic.domain.aggregates.apk.app.v1_0.rest.view_model.detail.apk_upload_detail import ApkUploadDetail
from pystatic.domain.aggregates.apk.model.apk import Apk

__author__ = 'H.Rouhani'


class ApkList:
    query_string = None
    storage_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        query_string_info = QueryStringInfo()
        search_info = query_string_info.load(self.query_string)
        apks = Apk.get_all(self.storage_name, search_info.skip, search_info.take)
        return ApkUploadDetail.create_apks_from_apks(apks)
