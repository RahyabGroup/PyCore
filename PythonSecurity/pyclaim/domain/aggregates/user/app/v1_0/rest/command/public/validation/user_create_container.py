from pyvalidate.validation import Validation

from pyclaim.domain.aggregates.user.model.validation.user_name_exist import UserNameExist

__author__ = 'Hooman'


class UserCreateContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.user_name, 3)
        super().string.size(self.instance.password, 5)
        super().string.size(self.instance.password, 8)
        super().validate()
        super().custom.register(self.instance.user_name.lower(), UserNameExist(None))
        super().validate()
