from pynotification.domain.aggregates.notification.model.notification import Notification

__author__ = 'root'


class Push:
    receiver_ids = None
    message_type = None
    data = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        for receiver_id in self.receiver_ids:
            notification = Notification()
            notification.receiver_id = receiver_id
            notification.message_type = self.message_type
            notification.data = self.data
            notification.create()




