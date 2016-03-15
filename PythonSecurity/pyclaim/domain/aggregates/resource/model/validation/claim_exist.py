from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceErrorCodes
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ClaimExist(Validation):
    def __init__(self, resource_id, claim_type_id):
        self.resource_id = resource_id
        self.claim_type_id = claim_type_id

    def validate(self, claim_value):
        resource = Resource()
        resource._id = self.resource_id
        exist_claim = resource.claim_exists(self.claim_type_id, claim_value)
        if exist_claim:
            super().custom.manual(ResourceErrorCodes.RESOURCE_CLAIM_EXIST)
