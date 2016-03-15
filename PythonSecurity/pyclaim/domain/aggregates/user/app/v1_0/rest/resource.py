from pyfacil.web.rest.resource import *

__author__ = 'H.Rouhani'


class UserErrorCodes(ErrorCodes):
    USER_USER_NAME_EXIST = {"body": "USER_USER_NAME_EXIST", "code": "err1008"}
    USER_CLAIM_ID_NOT_EXIST = {"body": "USER_CLAIM_ID_NOT_EXIST", "code": "err1009"}
    USER_CLAIM_EXIST = {"body": "USER_CLAIM_EXIST", "code": "err1010"}
    USER_ID_NOT_EXIST = {"body": "USER_ID_NOT_EXIST", "code": "err1011"}
    USER_NOT_AVAILABLE = {"body": "USER_NOT_AVAILABLE", "code": "err1012"}
    WRONG_PASSWORD = {"body": "WRONG_PASSWORD", "code": "err1015"}
    DEACTIVATED_USER = {"body": "DEACTIVATE_USER", "code": "err1016"}
    PROFILE_DEACTIVATED_BY_OTHER_USER = {"body": "PROFILE_DEACTIVATED_BY_OTHER_USER", "code": "err1017"}
    USER_ID_NOT_EQUAL_WITH_LOGGED_IN_USER_ID = {"body": "USER_ID_NOT_EQUAL_WITH_LOGGED_IN_USER_ID", "code": "err1018"}
    USER_IS_IN_AWAIT_STATUS = {"body": "USER_IS_IN_AWAIT_STATUS", "code": "err1019"}
    USER_IS_NOT_In_AWAIT_Status = {"body": "USER_IS_NOT_In_AWAIT_Status", "code": "err1025"}

class UserInfoCodes(InfoCodes):
    pass
