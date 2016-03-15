from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class UserWithUserNameNotExist(Validation):
    def validate(self, user_name):
        is_available_id = User.exist_with_user_name(user_name)
        if not is_available_id:
            super().custom.manual(UserErrorCodes.USER_NOT_AVAILABLE)
