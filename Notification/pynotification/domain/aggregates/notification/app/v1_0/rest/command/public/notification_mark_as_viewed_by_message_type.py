
from pynotification.domain.aggregates.notification.model.notification import Notification
from pynotification.main.assembler import auth

__author__ = 'root'


class NotificationMarkAsViewedByMessageType:
    message_type = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        Notification.mark_as_viewed_by_message_type(auth.user_id, self.message_type)
