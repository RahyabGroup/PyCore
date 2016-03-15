from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.model.validation.password_incorrect import PasswordIncorrect

__author__ = 'root'


class PasswordChangeContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance.old_password, PasswordIncorrect(self.instance.user_id))
        super().validate()
