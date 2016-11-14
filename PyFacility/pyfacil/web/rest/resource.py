__author__ = 'Hooman'


class ErrorCodes:
    SEARCH_SKIP_NOT_VALID = {"title": "SEARCH_SKIP_NOT_VALID", "code": "main_err01"}
    SEARCH_TAKE_NOT_VALID = {"title": "SEARCH_TAKE_NOT_VALID", "code": "main_err02"}
    INOPERABLE_PERSON_ERROR = {"title": "INOPERABLE_PERSON_ERROR", "code": "main_err03"}
    UNAUTHENTICATED_USER = {"title": "UNAUTHENTICATED_USER", "code": "main_err04"}
    UNAUTHORIZED_USER = {"title": "UNAUTHORIZED_USER", "code": "main_err05"}
    INTERNAL_SERVER_ERROR = {"title": "INTERNAL_SERVER_ERROR", "code": "main_err06"}
    FORBIDDEN = {"title": "FORBIDDEN", "code": "main_err07"}
    RESOURCE_NOT_FOUND = {"title": "RESOURCE_NOT_FOUND", "code": "main_err08"}
    USER_IS_NOT_OWNER = {"title": "USER_IS_NOT_OWNER", "code": "main_err09"}
    SEARCH_CRITERIA_IS_NOT_DEFINED = {"title": "SEARCH_CRITERIA_IS_NOT_DEFINED", "code": "main_err10"}
    INVALID_AUTH_CREDENTIALS = {"title": 'INVALID_AUTH_CREDENTIALS', "code": "err1010"}


class InfoCodes:
    DONE = {"title": "DONE", "code": "info1001"}
