from pyvalidate.validation import Validation
from pynotification.domain.aggregates.notification.app.v1_0.rest.resource import NotificationErrorCodes
from pynotification.domain.aggregates.notification.model.notification import Notification

__author__ = 'root'


class NotificationIdNotExists(Validation):
    def validate(self, notification_id):
        is_available_notification = Notification.id_exists(notification_id)
        if not is_available_notification:
            super().custom.manual(NotificationErrorCodes.NOTIFICATION_ID_NOT_EXIST)
