from pyfacil.security_client.pyclaim.flask.authentication import ClaimBasedAuthentication
from pyutil.method_call.async_call.async_invoker import AsyncInvoker
from pyvalidate.validation_decorator import ValidationDecorator
from pyclaim.main.config import Config

__author__ = 'H.Rouhani'

auth = ClaimBasedAuthentication(Config().security_url, Config().secret_key)
validator = ValidationDecorator()
async = AsyncInvoker()
