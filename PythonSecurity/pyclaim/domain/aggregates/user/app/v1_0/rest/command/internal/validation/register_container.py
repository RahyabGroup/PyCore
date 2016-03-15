from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.model.validation.user_name_exist import UserNameExist

__author__ = 'H.Rouhani'


class RegisterContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance.user_name.lower(), UserNameExist(None))
        super().validate()
