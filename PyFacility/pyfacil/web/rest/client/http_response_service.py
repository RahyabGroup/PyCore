from pyfacil.security_client.exceptions.authorization import AuthorizationError
from pyfacil.security_client.exceptions.authentication import AuthenticationError
from pyvalidate.exception.validation_exception import ValidationException
from werkzeug.exceptions import NotFound

__author__ = 'H.Rouhani'


def http_response_make(response):
    if response.status_code == 500:
        raise ValueError("Internal server error!")

    if response.status_code == 400:
        content_json = response.json()
        raise ValidationException(content_json["errors"] if isinstance(content_json["errors"], list) else [content_json["errors"]])

    if response.status_code == 401:
        raise AuthenticationError()

    if response.status_code == 405:
        raise AuthorizationError()

    if response.status_code == 403:
        raise NotFound()

    return response
