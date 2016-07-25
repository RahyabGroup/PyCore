from bson import ObjectId
from pyfacil.reposiotry.mongo.repository import Repository
from pynotification.main.config import Config

__author__ = 'root'


class NotificationWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(NotificationWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "notification", True)

    def view_status_change_by_id(self, notification_id, status):
        self._collection.writer.edit_by_condition({"_id": ObjectId(notification_id)},
                                                  {"$set": {"view_status": status}})

    def view_status_change_by_receiver_id_message_type(self, receiver_id, message_type, status):
        self._collection.writer.edit_by_condition({"$and": [{"receiver_id": receiver_id},
                                                            {"message_type": message_type}]},
                                                  {"$set": {"view_status": status}})
