from datetime import datetime
from functools import wraps

from bson.objectid import ObjectId, InvalidId
from flask import request
from pyutil.cryptography.rsa.object_coder import ObjectCoder
from pyfacil.security_client.exceptions.authentication import AuthenticationError
from pyfacil.security_client.exceptions.authorization import AuthorizationError
from pyfacil.web.rest.client.synchronous import requests

__author__ = 'Hooman'


class ClaimBasedAuthentication:
    def __init__(self, messaging_url, secret_key):
        self._messaging_url = messaging_url
        self._secret_key = secret_key

    def login_required(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                decrypted_token = self._get_decrypted_token()
                if not decrypted_token or not self._validate_token_lifetime(decrypted_token):
                    raise AuthenticationError()
                url = "{}{}{}{}".format(self._messaging_url, "/internal/token/", decrypted_token["token_id"], "/token_authenticated")
                result = requests.get(url)
                if not result or not result.json()["data"]:
                    raise AuthenticationError()
                return f(*args, **kwargs)

            return decorated_function

        return decorator

    def authorize(self):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                decrypted_token = self._get_decrypted_token()
                if not decrypted_token or not self._validate_token_lifetime(decrypted_token):
                    raise AuthenticationError()
                json_body = {"resource_name": f.__name__}
                url = "{}{}{}{}".format(self._messaging_url, "/internal/token/", decrypted_token["token_id"], "/token_authorize")
                result = requests.post(url, json=json_body).json()["data"]
                if not result or result == "Not Authorized":
                    raise AuthorizationError()
                if result == "Not Authenticated":
                    raise AuthenticationError()
                return f(*args, **kwargs)

            return decorated_function

        return decorator

    def is_owner(self, user_id):
        if self.is_sys_admin or user_id == self.user_id:
            return True
        return False

    def _get_user_id(self):
        decrypted_token = self._get_decrypted_token()
        if not decrypted_token:
            return None
        return decrypted_token["user_id"]

    def _is_sys_admin(self):
        decrypted_token = self._get_decrypted_token()
        if not decrypted_token:
            return False
        return decrypted_token["is_sys_admin"]

    def _get_decrypted_token(self):
        encrypted_token = request.headers.get('token')
        if not encrypted_token:
            return None
        decrypted_token = ObjectCoder(self._secret_key).decode(encrypted_token)
        return decrypted_token

    def _validate_token_lifetime(self, token):
        client_type = request.user_agent.platform
        if client_type in ['android', 'iphone', 'ipad']:
            return True
        try:
            oid_candidate = ObjectId(token["token_id"])
            if abs((datetime.utcnow() - oid_candidate.generation_time.replace(tzinfo=None)).total_seconds()) > 7 * 24 * 3600:
                return False
        except InvalidId:
            return False
        return True

    def _get_token(self):
        return request.headers.get('token')

    user_id = property(_get_user_id)
    is_sys_admin = property(_is_sys_admin)
    token = property(_get_token)
