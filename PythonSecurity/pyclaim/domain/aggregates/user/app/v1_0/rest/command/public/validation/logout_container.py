from pyvalidate.validation import Validation

__author__ = 'H.Rouhani'


class LogoutContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.token, 3)
        super().validate()
