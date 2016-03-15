from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.command.public.validation.claim_type_remove_container import \
    ClaimTypeRemoveContainer
from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ClaimTypeRemoveContainer)
class ClaimTypeRemove:
    _id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        claim_type = ClaimType()
        claim_type._id = self._id
        claim_type.remove()
        return "Done"
