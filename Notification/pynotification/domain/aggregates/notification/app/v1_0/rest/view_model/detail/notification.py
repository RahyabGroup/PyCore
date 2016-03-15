__author__ = 'root'


class NotificationDetail:
    _id = None
    receiver_id = None
    message_type = None
    data = None
    # mark_as_viewed = None

    def __init__(self):
        self.receiver_id = []
        self.data = []

    @staticmethod
    def create_from_notification(notification):
        if notification:
            notification_detail = NotificationDetail()
            notification_detail._id = notification._id
            notification_detail.receiver_id = notification.receiver_id
            notification_detail.message_type = notification.message_type
            notification_detail.data = notification.data
            # notification_detail.mark_as_viewed = notification.mark_as_viewed
            return notification_detail
        return None


    @staticmethod
    def create_from_notifications(notifications):
        result = []
        if notifications:
            for notification in notifications:
                result.append(NotificationDetail.create_from_notification(notification))
        return result