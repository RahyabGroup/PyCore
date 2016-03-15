from pyfacil.web.rest.resource import ErrorCodes
from pyvalidate.validation import Validation
from pynotification.main.assembler import auth

__author__ = 'root'


class NotificationGetByReceiverIdValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.message_type, 3, 50, True)
        super().list.size(self.instance.query_string, 2, 2, True)
        super().validate()
        if not auth.is_owner(self.instance.receiver_id):
            super().custom.manual(ErrorCodes.USER_IS_NOT_OWNER)
        super().validate()
