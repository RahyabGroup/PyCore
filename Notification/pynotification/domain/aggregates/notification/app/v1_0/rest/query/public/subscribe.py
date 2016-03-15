from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.validation.notification_get_updates_validator import \
    NotificationGetUpdatesValidator
from pynotification.domain.services.notification_latest_change import NotificationLatestChangeListener
from pynotification.main.assembler import validator

__author__ = 'root'


@validator.validation(NotificationGetUpdatesValidator)
class Subscribe:
    receiver_id = None
    message_type = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        notification_latest_change_listener_service = NotificationLatestChangeListener()
        notification_latest_change_listener_service.receiver_id = self.receiver_id
        notification_latest_change_listener_service.message_type = self.message_type
        yield from notification_latest_change_listener_service.execute()
