from pyfacil.web.rest.resource import *

__author__ = 'Hooman'


class NotificationErrorCodes(ErrorCodes):
    NOTIFICATION_ID_NOT_EXIST = {"title": "NOTIFICATION_ID_NOT_EXIST", "code": "err_notification_01"}
    RECEIVER_ID_NOT_EXIST = {"title": "RECEIVER_ID_NOT_EXIST", "code": "err_notification_02"}
    RECEIVER_ID_NOT_EQUALS_RECEIVER_ID = {"title": "RECEIVER_ID_NOT_EQUALS_RECEIVER_ID", "code": "err_notification_03"}

class NotificationInfoCodes(InfoCodes):
    pass
