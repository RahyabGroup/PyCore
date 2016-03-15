from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.command.public.validation.claim_type_create_container import \
    ClaimTypeCreateContainer

from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ClaimTypeCreateContainer)
class ClaimTypeCreate:
    name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        claim_type = ClaimType()
        claim_type.name = self.name
        claim_type.create()
        return claim_type._id
