from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceErrorCodes
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ClaimIdNotExist(Validation):
    def __init__(self, resource_id):
        self.resource_id = resource_id

    def validate(self, claim_id):
        resource = Resource()
        resource._id = self.resource_id
        claim_id_exist = resource.claim_id_exists(claim_id)
        if not claim_id_exist:
            super().custom.manual(ResourceErrorCodes.RESOURCE_CLAIM_ID_NOT_EXIST)
