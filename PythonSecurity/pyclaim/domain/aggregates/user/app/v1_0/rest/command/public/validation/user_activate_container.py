from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.model.validation.user_id_not_exist import UserIdNotExist

__author__ = 'Hooman'


class UserActivateContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.user_id, 5, 50)
        super().custom.register(self.instance.user_id, UserIdNotExist())
        super().validate()
