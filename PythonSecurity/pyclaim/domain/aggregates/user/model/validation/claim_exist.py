from pyvalidate.validation import Validation

from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class ClaimExist(Validation):
    def __init__(self, user_id, claim_type_id):
        self.user_id = user_id
        self.claim_type_id = claim_type_id

    def validate(self, claim_value):
        user = User()
        user._id = self.user_id
        exist_claim = user.claim_exist(self.claim_type_id, claim_value)
        if exist_claim:
            super().custom.manual(UserErrorCodes.USER_CLAIM_EXIST)
