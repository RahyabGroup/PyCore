from pyfacil.security_client.exceptions.inoperable_user import InoperableUserError
from pyfacil.security_client.exceptions.authorization import AuthorizationError
from pyfacil.security_client.exceptions.authentication import AuthenticationError
from pyvalidate.exception.validation_exception import ValidationException
from pyfacil.web.rest.flask import main_handler
from pyfacil.web.rest.resource import ErrorCodes

__author__ = 'Hooman'

from flask import jsonify, make_response
from pyutil.serialization.json.serializer import Serializer


@main_handler.app_errorhandler(404)
def page_not_found(e):
    response = _response_get(ErrorCodes.RESOURCE_NOT_FOUND, is_error=True)
    response.status_code = 404
    return response


@main_handler.app_errorhandler(500)
def internal_server_error(e):
    if isinstance(e, ValidationException):
        return bad_request(e.Errors)
    if isinstance(e, AuthenticationError):
        return unauthenticated()
    if isinstance(e, AuthorizationError) or isinstance(e, InoperableUserError):
        return unauthorized()
    response = _response_get(ErrorCodes.INTERNAL_SERVER_ERROR, is_error=True)
    response.status_code = 500
    return response


def created(data, meta=None):
    response = _response_get(data, meta=meta)
    response.status_code = 201
    return response


def ok(data, meta=None):
    response = _response_get(data, meta=meta)
    response.status_code = 200
    return response


def bad_request(data):
    response = _response_get(data, is_error=True)
    response.status_code = 400
    return response


def unauthorized():
    response = _response_get(ErrorCodes.UNAUTHORIZED_USER, is_error=True)
    response.status_code = 401
    return response


def forbidden():
    response = _response_get(ErrorCodes.FORBIDDEN, is_error=True)
    response.status_code = 403
    return response


def unauthenticated():
    response = _response_get(ErrorCodes.UNAUTHENTICATED_USER, is_error=True)
    response.status_code = 405
    return response


def make_send_file_response(file_content, file_name):
    response = make_response(file_content)
    response.headers["Content-Disposition"] = "attachment; filename=%s" % file_name
    return response


def _response_get(data, meta=None, is_error=False):
    key = "data"
    if is_error:
        key = "errors"
    result = {key: data}
    if meta:
        result["meta"] = meta
    serializer = Serializer()
    dict_result = serializer.serialize_to_dictionary(result, False)
    response = jsonify(dict_result)
    return _response_set_detail_access(response)


def _response_set_detail_access(response):
    response.headers['Access-Control-Allow-Origin'] = '*'   #'http://localhost:63343'
    response.headers['Access-Control-Expose-Headers'] = 'token'
    # response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    # response.headers['Access-Control-Allow-Headers'] = 'true'
    # response.headers['Access-Control-Max-Age'] = '1'
    # response.headers['Access-Control-Allow-Credentials'] = True
    return response
