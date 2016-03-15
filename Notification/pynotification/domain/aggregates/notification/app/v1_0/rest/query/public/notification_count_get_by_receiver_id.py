from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.validation.notification_count_get_by_receiver_id_validator import \
    NotificationCountGetByReceiverIdValidator
from pynotification.domain.aggregates.notification.model.notification import Notification
from pynotification.main.assembler import validator

__author__ = 'root'


@validator.validation(NotificationCountGetByReceiverIdValidator)
class NotificationCountGetByReceiverId:
    receiver_id = None
    message_type = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        notification_count_of_user = Notification.notification_count_get_by_receiver_id(self.receiver_id, self.message_type)
        return notification_count_of_user

