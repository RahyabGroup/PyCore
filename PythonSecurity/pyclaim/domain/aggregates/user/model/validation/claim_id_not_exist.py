from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class ClaimIdNotExist(Validation):
    def __init__(self, user_id):
        self.user_id = user_id

    def validate(self, claim_id):
        user = User()
        user._id = self.user_id
        claim_id_exist = user.claim_id_exist(claim_id)
        if not claim_id_exist:
            super().custom.manual(UserErrorCodes.USER_CLAIM_ID_NOT_EXIST)
