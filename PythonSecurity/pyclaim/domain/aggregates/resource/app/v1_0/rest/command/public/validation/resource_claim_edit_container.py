from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.model.validation.claim_exist import ClaimExist
from pyclaim.domain.aggregates.resource.model.validation.resource_id_not_exist import ResourceIdNotExist

__author__ = 'Hooman'


class ResourceClaimEditContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance._id, ResourceIdNotExist())
        super().custom.register(self.instance.claim_value, ClaimExist(self.instance._id, self.instance.claim_type_id))
        super().string.size(self.instance._id, 3)
        super().string.size(self.instance.claimId, 3)
        super().string.size(self.instance.claimTypeId, 3)
        super().string.size(self.instance.claimValue, 3)
        super().validate()
