from bson import ObjectId
from pynotification.domain.aggregates.notification.app.v1_0.rest.assembler import *

from pynotification.domain.aggregates.notification.model.notification_view_status import NotificationViewStatus

__author__ = 'root'


class Notification:
    _id = None
    receiver_id = None
    message_type = None
    data = None
    view_status = None

    def __init__(self):
        self._id = str(ObjectId())
        self.receiver_id = None
        self.data = []
        self.view_status = NotificationViewStatus.not_viewed

    @staticmethod
    def id_exists(notification_id):
        return notification_reader.exist_id(notification_id)

    @staticmethod
    def notification_new_updates_by_receiver_id_and_message_type(receiver_id, message_type, current_id):
        return notification_reader.notification_new_updates_by_receiver_id_and_message_type(receiver_id, message_type,
                                                                                        current_id)

    @staticmethod
    def notification_get_by_receiver_id(receiver_id, message_type, skip, take, sort):
        return notification_reader.notification_get_by_receiver_id(receiver_id, message_type, skip, take, sort)

    @staticmethod
    def notification_count_get_by_receiver_id(receiver_id, message_type):
        return notification_reader.notification_count_get_by_receiver_id(receiver_id, message_type)

    @staticmethod
    def receiver_exists(notification_id, receiver_id):
        return notification_reader.receiver_exists(notification_id, receiver_id)

    @staticmethod
    def mark_as_viewed_by_message_type(receiver_id, message_type):
        notification_writer.view_status_change_by_receiver_id_message_type(receiver_id, message_type,
                                                                           NotificationViewStatus.viewed)

    def create(self):
        notification_writer.create(self)

    def mark_as_viewed_by_id(self):
        notification_writer.view_status_change_by_id(self._id, NotificationViewStatus.viewed)
