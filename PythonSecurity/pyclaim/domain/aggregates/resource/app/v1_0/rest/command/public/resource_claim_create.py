from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_claim_create_container import \
    ResourceClaimCreateContainer
from pyclaim.domain.aggregates.resource.model.claim import Claim
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceClaimCreateContainer)
class ResourceClaimCreate:
    _id = None
    claim_type_id = None
    claim_value = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource._id = self._id
        resource_claim = Claim()
        resource_claim.claim_type_id = self.claim_type_id
        resource_claim.value = self.claim_value
        resource.claim_add(resource_claim)
        return resource_claim._id
