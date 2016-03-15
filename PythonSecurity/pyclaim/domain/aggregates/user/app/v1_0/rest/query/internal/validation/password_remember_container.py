from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.model.validation.user_with_user_name_not_exist import UserWithUserNameNotExist

__author__ = 'Amir H. Nejati'


class PasswordRememberContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance.query_string["user_name"], UserWithUserNameNotExist())
        super().validate()
