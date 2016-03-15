from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes

from pyclaim.main.assembler import auth

__author__ = 'H.Rouhani'


class UserGetByIdContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        if not auth.is_owner(self.instance.user_id):
            super().custom.manual(UserErrorCodes.USER_IS_NOT_OWNER)
        super().validate()
