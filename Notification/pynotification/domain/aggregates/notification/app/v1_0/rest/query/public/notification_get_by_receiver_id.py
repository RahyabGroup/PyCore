from pyfacil.web.query_string.query_string_info import QueryStringInfo
from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.validation.notification_get_by_receiver_id_validator import \
    NotificationGetByReceiverIdValidator
from pynotification.domain.aggregates.notification.app.v1_0.rest.view_model.detail.notification import \
    NotificationDetail
from pynotification.domain.aggregates.notification.model.notification import Notification
from pynotification.main.assembler import validator

__author__ = 'root'


@validator.validation(NotificationGetByReceiverIdValidator)
class NotificationGetByReceiverId:
    receiver_id = None
    message_type = None
    query_string = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        query_string_info = QueryStringInfo()
        query_string_info.load(self.query_string)
        notifications = Notification.notification_get_by_receiver_id(self.receiver_id, self.message_type, query_string_info.skip,
                                                                     query_string_info.take, query_string_info.sort)
        return NotificationDetail.create_from_notifications(notifications)
