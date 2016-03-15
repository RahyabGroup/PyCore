from pyvalidate.validation import Validation


__author__ = 'root'


class NotificationGetUpdatesValidator(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.receiver_id, 3, 50, True)
        super().string.size(self.instance.message_type, 3, 50, True)
        super().validate()
