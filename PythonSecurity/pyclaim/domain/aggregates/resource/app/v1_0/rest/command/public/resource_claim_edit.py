from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_claim_edit_container import \
    ResourceClaimEditContainer
from pyclaim.domain.aggregates.resource.model.claim import Claim
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceClaimEditContainer)
class ResourceClaimEdit:
    _id = None
    claim_id = None
    claim_type_id = None
    claim_value = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource._id = self._id
        resource_claim = Claim()
        resource_claim._id = self.claim_id
        resource_claim.claim_type_id = self.claim_type_id
        resource_claim.value = self.claim_value
        resource.claim_edit(resource_claim)
        return "Done"
