from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.model.validation.resource_id_not_exist import ResourceIdNotExist

from pyclaim.domain.aggregates.resource.model.validation.claim_id_not_exist import ClaimIdNotExist
from pyclaim.domain.aggregates.resource.model.validation.resource_permission_claim_is_not_removable import \
    ResourcePermissionClaimIsNotRemovable

__author__ = 'Hooman'


class ResourceClaimRemoveContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance._id, 3)
        super().string.size(self.instance.claimId, 3)
        super().custom.register(self.instance._id, ResourceIdNotExist())
        super().custom.register(self.instance.claim_id, ClaimIdNotExist(self.instance._id))
        super().custom.register(self.instance.claim_id, ResourcePermissionClaimIsNotRemovable(self.instance._id))
        super().validate()
