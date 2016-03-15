from flask import request
from pyfacil.web.rest.flask.response import *
from pynotification.domain.aggregates.notification.app.v1_0.rest import apis

from pynotification.domain.aggregates.notification.app.v1_0.rest.command.internal.push import Push
from pynotification.domain.aggregates.notification.app.v1_0.rest.resource import NotificationInfoCodes

__author__ = 'root'


@apis.route('/internal/notification', methods=['POST'])
def push():
    dto = request.get_json()
    push_command = Push(dto)
    push_command.execute()
    return created(NotificationInfoCodes.DONE)

