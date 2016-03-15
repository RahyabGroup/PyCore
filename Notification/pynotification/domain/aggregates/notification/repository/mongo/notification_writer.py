from bson import ObjectId
from pyfacil.reposiotry.mongo.repository import Repository
from pynotification.main.config import Config

__author__ = 'root'


class NotificationWriter(Repository):
    def __init__(self):
        cfg = Config()
        super(NotificationWriter, self).__init__(cfg.mongo_connection, cfg.mongo_db_name, "notification", True)

    def view_status_change(self, notification_id, status):
        self._collection.writer.edit_by_condition({"_id": ObjectId(notification_id)},
                                                 {"$set": {"view_status": status}})

