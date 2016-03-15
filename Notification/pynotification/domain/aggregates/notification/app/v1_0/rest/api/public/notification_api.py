from pyfacil.web.rest.flask.response import *
from pynotification.domain.aggregates.notification.app.v1_0.rest import apis
from pynotification.domain.aggregates.notification.app.v1_0.rest.command.public.notification_mark_as_viewed import \
    NotificationMarkAsViewed
from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.notification_count_get_by_receiver_id import \
    NotificationCountGetByReceiverId
from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.notification_get_by_receiver_id import \
    NotificationGetByReceiverId
from pynotification.domain.aggregates.notification.app.v1_0.rest.query.public.subscribe import \
    Subscribe
from pynotification.domain.aggregates.notification.app.v1_0.rest.resource import NotificationInfoCodes
from pynotification.main.assembler import auth

__author__ = 'H.Rouhani'
from flask import request, Response


@apis.route('/notification/<receiver_id>/<message_type>', methods=['GET'])
def subscribe(receiver_id, message_type):
    dto = {'receiver_id': receiver_id, 'message_type': message_type}
    subscribe_command = Subscribe(dto)
    response = Response(subscribe_command.execute(), mimetype="text/event-stream", status=200)
    return response


@apis.route('/notification/receiver/<receiver_id>/message_type/<message_type>', methods=['GET'])
@auth.login_required()
def notification_get_by_receiver_id(receiver_id, message_type):
    dto = {"message_type": message_type, "query_string": request.args, "receiver_id": receiver_id}
    notification_get_by_receiver_id_reader = NotificationGetByReceiverId(dto)
    notification_list = notification_get_by_receiver_id_reader.execute()
    return ok(notification_list)


@apis.route('/notification/receiver/<receiver_id>/message_type/<message_type>/count', methods=["GET"])
@auth.login_required()
def notification_count_get_by_receiver_id(receiver_id, message_type):
    dto = {"message_type": message_type, "receiver_id": receiver_id}
    notification_count_get_by_receiver_id_reader = NotificationCountGetByReceiverId(dto)
    notification_count = notification_count_get_by_receiver_id_reader.execute()
    return ok(notification_count)


@apis.route('/notification/<notification_id>', methods=["PUT"])
@auth.login_required()
def notification_mark_as_viewed(notification_id):
    dto = {"notification_id": notification_id}
    notification_mark_as_viewed_command = NotificationMarkAsViewed(dto)
    notification_mark_as_viewed_command.execute()
    return ok(NotificationInfoCodes.DONE)
