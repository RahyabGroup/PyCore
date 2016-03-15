from pyfacil.web.rest.resource import *

__author__ = 'Hooman'


class FileErrorCodes(ErrorCodes):
    RESOURCE_CONTENT_IS_EMPTY = {"title": "RESOURCE_CONTENT_IS_EMPTY", "code": "err_file_01"}
    FILE_EXTENSION_IS_NOT_VALID = {"title": "FILE_EXTENSION_IS_NOT_VALID", "code": "err_file_02"}
    FILE_ID_NOT_EXIST = {"title": "FILE_ID_NOT_EXIST", "code": "err_file_03"}
    FILE_NAME_OR_EXTENSION_NOT_EXIST = {"title": "FILE_NAME_OR_EXTENSION_NOT_EXIST", "code": "err_file_04"}
    FILE_NAME_IS_INVALID = {"title": "FILE_NAME_IS_INVALID", "code": "err_file_05"}


class FileInfoCodes(InfoCodes):
    pass
