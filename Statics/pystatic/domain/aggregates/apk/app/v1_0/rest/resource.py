from pyfacil.web.rest.resource import *

__author__ = 'Hooman'


class ApkErrorCodes(ErrorCodes):
    RESOURCE_CONTENT_IS_EMPTY = {"title": "RESOURCE_CONTENT_IS_EMPTY", "code": "err_apk_01"}
    APK_EXTENSION_IS_NOT_VALID = {"title": "APK_EXTENSION_IS_NOT_VALID", "code": "err_apk_02"}
    APK_FILE_NAME_EXIST = {"title": "APK_FILE_NAME_EXIST", "code": "err_apk_03"}
    APK_FILE_NAME_NOT_EXIST = {"title": "APK_FILE_NAME_NOT_EXIST", "code": "err_apk_04"}
    APK_VERSION_ID_NOT_EXIST = {"title": "APK_VERSION_ID_NOT_EXIST", "code": "err_apk_05"}
    APK_VERSION_ID_EXIST = {"title": "APK_VERSION_ID_EXIST", "code": "err_apk_06"}
    APK_NAME_OR_EXTENSION_NOT_EXIST = {"title": "APK_NAME_OR_EXTENSION_NOT_EXIST", "code": "err_apk_07"}

class ApkInfoCodes(InfoCodes):
    pass
