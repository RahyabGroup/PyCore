from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class PasswordIncorrect(Validation):
    def __init__(self, user_id):
        self.user_id = user_id

    def validate(self, password):
        user = User()
        user._id = self.user_id
        is_available_id = user.password_exist(password)
        if not is_available_id:
            super().custom.manual(UserErrorCodes.WRONG_PASSWORD)
