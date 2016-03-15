from bson import ObjectId

from pyutil.serialization.json.serializer import Serializer
import time
from pynotification.domain.aggregates.notification.model.notification import Notification

__author__ = 'H.Rouhani'


class NotificationLatestChangeListener:
    receiver_id = None
    message_type = None

    def execute(self):
        json_serializer = Serializer()
        current_id = str(ObjectId())
        while True:
            time.sleep(5)
            try:
                notifications = Notification.notification_new_updates_by_receiver_id_and_message_type(self.receiver_id, self.message_type, current_id)
                if notifications:
                    current_id = notifications[0]._id
                    serialized_notification = json_serializer.serialize_to_string(notifications)
                    result = "data:{}{}".format(serialized_notification, '\nretry:500\n\n')
                    yield result
            except StopIteration:
                continue
