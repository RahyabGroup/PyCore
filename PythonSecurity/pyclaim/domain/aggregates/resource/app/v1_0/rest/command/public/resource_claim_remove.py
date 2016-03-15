from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_claim_remove_container import \
    ResourceClaimRemoveContainer
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceClaimRemoveContainer)
class ResourceClaimRemove:
    _id = None
    claim_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource._id = self._id
        resource.claim_remove(self.claim_id)
        return "Done"
