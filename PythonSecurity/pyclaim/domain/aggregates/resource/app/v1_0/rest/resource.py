from pyfacil.web.rest.resource import *

__author__ = 'H.Rouhani'


class ResourceErrorCodes(ErrorCodes):
    RESOURCE_NAME_EXIST = {"body": "RESOURCE_NAME_EXIST", "code": "err1004"}
    RESOURCE_ID_NOT_EXIST = {"body": "RESOURCE_ID_NOT_EXIST", "code": "err1007"}
    RESOURCE_CLAIM_WITH_PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE = {"body": "RESOURCE_CLAIM_WITH_PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE", "code": "err1014"}
    RESOURCE_CLAIM_EXIST = {"body": "RESOURCE_CLAIM_EXIST", "code": "err1020"}
    RESOURCE_CLAIM_ID_NOT_EXIST = {"body": "RESOURCE_CLAIM_ID_NOT_EXIST", "code": "err1021"}

class ResourceInfoCodes(InfoCodes):
    pass
