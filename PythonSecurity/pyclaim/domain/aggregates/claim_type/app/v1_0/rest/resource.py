from pyfacil.web.rest.resource import *

__author__ = 'H.Rouhani'


class ClaimTypeErrorCodes(ErrorCodes):
    CLAIM_TYPE_NAME_EXIST = {"body": "CLAIM_TYPE_NAME_EXIST", "code": "err1001"}
    CLAIM_TYPE_USAGE = {"body": "CLAIM_TYPE_USAGE", "code": "err1002"}
    CLAIM_TYPE_ID_NOT_EXIST = {"body": "CLAIM_TYPE_ID_NOT_EXIST", "code": "err1003"}
    PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE = {"body": "PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE", "code": "err1013"}


class ClaimTypeInfoCodes(InfoCodes):
    pass
