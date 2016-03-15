from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.model.validation.claim_exist import ClaimExist
from pyclaim.domain.aggregates.user.model.validation.user_id_not_exist import UserIdNotExist

__author__ = 'Hooman'


class UserClaimCreateContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance._id, 3)
        super().string.size(self.instance.claimTypeId, 3)
        super().string.size(self.instance.claimValue, 3)
        super().custom.register(self.instance._id, UserIdNotExist())
        super().custom.register(self.instance.claimValue, ClaimExist(self.instance._id, self.instance.claimTypeId))
        super().validate()
