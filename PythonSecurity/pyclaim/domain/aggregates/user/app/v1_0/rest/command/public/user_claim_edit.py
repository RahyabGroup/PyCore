from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_claim_edit_container import \
    UserClaimEditContainer
from pyclaim.domain.aggregates.user.model.claim import Claim
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserClaimEditContainer)
class UserClaimEdit:
    _id = None
    claim_id = None
    claim_type_id = None
    claim_value = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.get_by_id(self._id)
        user_claim = Claim()
        user_claim._id = self.claim_id
        user_claim.claim_type_id = self.claim_type_id
        user_claim.value = self.claim_value
        user.claim_edit(user_claim)
        return "Done"
