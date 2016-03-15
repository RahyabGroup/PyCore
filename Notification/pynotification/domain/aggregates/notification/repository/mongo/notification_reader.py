from bson import ObjectId
from pyfacil.reposiotry.mongo.searcher import Searcher

from pynotification.domain.aggregates.notification.model.notification_view_status import NotificationViewStatus
from pynotification.main.config import Config

__author__ = 'root'


class NotificationReader(Searcher):
    def __init__(self):
        cfg = Config()
        super(NotificationReader, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "notification", True)

    def notification_get_by_receiver_id(self, receiver_id, message_type, skip, take, sort):
        search_query = {'$and': [{"receiver_id": receiver_id},
                                 {"message_type": message_type},
                                 {"view_status": NotificationViewStatus.not_viewed}]}
        return self._collection.reader.find_many(query=search_query, skip=skip, take=take, sort=sort)

    def notification_count_get_by_receiver_id(self, receiver_id, message_type):
        search_query = {'$and': [{"receiver_id": receiver_id},
                                 {"message_type": message_type},
                                 {"view_status": NotificationViewStatus.not_viewed}]}
        return self._collection.reader.count(search_query)

    def notification_new_updates_by_receiver_id_and_message_type(self, receiver_id, message_type, greater_than_id):
        query = {'$and': [{"receiver_id": receiver_id},
                          {"message_type": message_type},
                          {"view_status": NotificationViewStatus.not_viewed},
                          {"_id": {"$gt": ObjectId(greater_than_id)}}]}
        cursor = self._collection.reader.open_tailable_cursor(query)

        notifications = []
        for notification in cursor:
            notifications.append(self._collection.reader._get_result(notification))

        return notifications
    
    def receiver_exists(self, notification_id, receiver_id):
        search_query = {"$and": [{"_id": ObjectId(notification_id)},
                                 {"receiver_id": receiver_id}]}
        return self._collection.reader.is_available(search_query)

