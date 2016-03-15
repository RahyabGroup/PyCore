from pyvalidate.validation import Validation


from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceErrorCodes
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'H.Rouhani'


class ResourcePermissionClaimIsNotRemovable(Validation):
    def __init__(self, resource_id):
        self.resource_id = resource_id

    def validate(self, claim_id):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        permission_claim_type = ClaimType.get_permission()
        resource = Resource()
        resource._id = self.resource_id
        claim_is_of_claim_type = resource.claim_is_of_claim_type(claim_id, permission_claim_type._id)
        if claim_is_of_claim_type:
            super().custom.manual(ResourceErrorCodes.RESOURCE_CLAIM_WITH_PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE)

