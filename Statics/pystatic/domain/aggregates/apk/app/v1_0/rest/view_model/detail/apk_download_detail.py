__author__ = 'H.Rouhani'


class ApkDownloadDetail:
    apk_name = None
    apk_content = None

    @staticmethod
    def create_from_apk(apk):
        if apk:
            apk_detail = ApkDownloadDetail()
            apk_detail.apk_name = apk.persisted_file_name
            apk_detail.apk_content = apk.content
            return apk_detail
        return None