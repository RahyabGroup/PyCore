from pyvalidate.validation import Validation

__author__ = 'Hooman'


class LoginContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.user_name, 3)
        super().string.size(self.instance.password, 8)
        super().validate()
