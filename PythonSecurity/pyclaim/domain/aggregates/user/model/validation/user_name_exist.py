from pyvalidate.validation import Validation

from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class UserNameExist(Validation):
    def __init__(self, user_id):
        self._user_id = user_id

    def validate(self, user_user_name):
        user_with_user_name = User.get_by_user_name(user_user_name)
        user_name_exists = UserErrorCodes.USER_USER_NAME_EXIST
        user_name_exists["data"] = user_user_name
        if user_with_user_name is None:
            return None
        elif not self._user_id:
            super().custom.manual(user_name_exists)

        if user_with_user_name._id != self._user_id:
            super().custom.manual(user_name_exists)
