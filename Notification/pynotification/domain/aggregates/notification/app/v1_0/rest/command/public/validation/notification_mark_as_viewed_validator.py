from pyfacil.web.rest.resource import ErrorCodes
from pyvalidate.validation import Validation
from pynotification.domain.aggregates.notification.model.notification import Notification
from pynotification.domain.aggregates.notification.model.validation.notification_id_not_exists import \
    NotificationIdNotExists
from pynotification.main.assembler import auth

__author__ = 'root'


class NotificationMarkAsViewedValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.notification_id, 3, 50, True)
        super().validate()
        super().custom.register(self.instance.notification_id, NotificationIdNotExists(), True)
        super().validate()
        if not Notification.receiver_exists(self.instance.notification_id, auth.user_id):
            super().custom.manual(ErrorCodes.USER_IS_NOT_OWNER)
        super().validate()
