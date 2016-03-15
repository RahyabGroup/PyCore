from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.main.assembler import auth

__author__ = 'H.Rouhani'


class UserIdControl(Validation):
    def validate(self, user_id):
        if auth.user_id != user_id:
            super().custom.manual(UserErrorCodes.USER_ID_NOT_EQUAL_WITH_LOGGED_IN_USER_ID)
