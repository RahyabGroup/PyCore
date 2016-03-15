from pyvalidate.validation import Validation

from pyclaim.domain.aggregates.user.model.validation.user_name_exist import UserNameExist
from pyclaim.main.assembler import auth

__author__ = 'Hooman'


class UserEditContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance.user_name.lower(), UserNameExist(auth.user_id))
        super().string.size(self.instance.user_name, 3)
        super().string.size(self.instance.password, 8)
        super().validate()
