__author__ = 'root'


class ApkUploadDetail:
    apk_name = None
    apk_path = None
    apk_version_id = None
    apk_upload_date = None

    @staticmethod
    def create_from_apk(apk):
        if apk:
            apk_upload_detail = ApkUploadDetail()
            apk_upload_detail.apk_name = apk.persisted_file_name
            apk_upload_detail.apk_path = apk.path
            apk_upload_detail.apk_version_id = apk.version.version_id
            apk_upload_detail.apk_upload_date = apk.upload_date
            return apk_upload_detail
        return None

    @staticmethod
    def create_apks_from_apks(apks):
        result = []
        if apks:
            for apk in apks:
                result.append(ApkUploadDetail.create_from_apk(apk))
        return result
