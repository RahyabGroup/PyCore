from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_claim_create_container import \
    UserClaimCreateContainer
from pyclaim.domain.aggregates.user.model.claim import Claim
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserClaimCreateContainer)
class UserClaimCreate:
    _id = None
    claim_type_id = None
    claim_value = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = self._id
        user_claim = Claim()
        user_claim.claim_type_id = self.claim_type_id
        user_claim.value = self.claim_value
        user.claim_add(user_claim)
        return user_claim._id
