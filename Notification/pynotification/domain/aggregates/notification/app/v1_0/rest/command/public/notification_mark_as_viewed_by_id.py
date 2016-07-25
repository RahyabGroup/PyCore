from pynotification.domain.aggregates.notification.app.v1_0.rest.command.public.validation.notification_mark_as_viewed_validator import \
    NotificationMarkAsViewedValidator
from pynotification.domain.aggregates.notification.model.notification import Notification
from pynotification.main.assembler import validator

__author__ = 'root'


@validator.validation(NotificationMarkAsViewedValidator)
class NotificationMarkAsViewedById:
    notification_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        notification = Notification()
        notification.view_status = 1
        notification._id = self.notification_id
        notification.mark_as_viewed_by_id()
