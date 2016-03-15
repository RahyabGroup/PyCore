from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.validation.user_claim_remove_container import \
    UserClaimRemoveContainer
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserClaimRemoveContainer)
class UserClaimRemove:
    _id = None
    claim_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.get_by_id(self._id)
        user.claim_remove(self.claim_id)
        return "Done"
