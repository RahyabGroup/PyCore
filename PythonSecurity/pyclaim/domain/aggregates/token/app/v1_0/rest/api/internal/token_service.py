from flask import request
from pyfacil.web.rest.flask.response import *

from pyclaim.domain.aggregates.token.app.v1_0.rest import apis
from pyclaim.domain.aggregates.token.app.v1_0.rest.command.internal.request_generate_token_instance import RequestGenerateTokenInstance
from pyclaim.domain.aggregates.token.app.v1_0.rest.command.internal.request_token_remove import RequestTokenRemove
from pyclaim.domain.aggregates.token.app.v1_0.rest.command.internal.user_removed_token import UserRemovedToken
from pyclaim.domain.aggregates.token.app.v1_0.rest.query.internal.request_token_authenticated import RequestTokenAuthenticated
from pyclaim.domain.aggregates.token.app.v1_0.rest.query.internal.request_token_authorize import RequestTokenAuthorize
from pyclaim.domain.aggregates.token.app.v1_0.rest.query.internal.request_token_get_by_id import RequestTokenGetById
from pyclaim.domain.aggregates.token.app.v1_0.rest.resource import TokenInfoCodes


__author__ = 'H.Rouhani'


@apis.route('/internal/tokens/<token_id>', methods=['GET'])
def request_token_get_by_id(token_id):
    dto = {"token_id": token_id}
    request_token_get_by_id_reader = RequestTokenGetById(dto)
    result = request_token_get_by_id_reader.execute()
    return ok(result)


@apis.route('/internal/token/<token_id>/token_authenticated', methods=['GET'])
def request_token_authenticated(token_id):
    dto = {"token_id": token_id}
    request_token_authenticate_reader = RequestTokenAuthenticated(dto)
    result = request_token_authenticate_reader.execute()
    return ok(result)


@apis.route('/internal/token/<token_id>/token_authorize', methods=['POST'])
def request_token_authorize(token_id):
    dto = request.get_json()
    dto["token_id"] = token_id
    request_token_authorize_reader = RequestTokenAuthorize(dto)
    result = request_token_authorize_reader.execute()
    return ok(result)


@apis.route('/internal/tokens', methods=['POST'])
def request_token_generate_instance():
    dto = request.get_json()
    request_generate_token_instance_command = RequestGenerateTokenInstance(dto)
    result = request_generate_token_instance_command.execute()
    return ok(result)


@apis.route('/internal/tokens/<token_id>', methods=['DELETE'])
def request_token_remove(token_id):
    dto = {"token_id": token_id}
    request_token_remove_command = RequestTokenRemove(dto)
    request_token_remove_command.execute()
    return ok(TokenInfoCodes.DONE)


@apis.route('/internal/token/user/<user_id>', methods=['DELETE'])
def subscribe_user_removed_token(user_id):
    dto = {"user_id": user_id}
    user_changed_token_command = UserRemovedToken(dto)
    user_changed_token_command.execute()
    return ok(TokenInfoCodes.DONE)
