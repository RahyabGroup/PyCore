from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class UserIdNotExist(Validation):
    def validate(self, _id):
        is_available_id = User.id_exists(_id)
        if not is_available_id:
            super().custom.manual(UserErrorCodes.USER_ID_NOT_EXIST)
