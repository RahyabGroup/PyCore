from pynotification.domain.aggregates.notification.repository.mongo.notification_reader import NotificationReader
from pynotification.domain.aggregates.notification.repository.mongo.notification_writer import NotificationWriter

__author__ = 'Hooman Familrouhani'


notification_reader = NotificationReader()
notification_writer = NotificationWriter()