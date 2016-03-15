from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.claim_type.model.validation.claim_type_id_not_exist import ClaimTypeIdNotExist
from pyclaim.domain.aggregates.claim_type.model.validation.permission_claim_type_not_removable import \
    PermissionClaimTypeNotRemovable

__author__ = 'Hooman'


class ClaimTypeRemoveContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance._id, 1)
        super().custom.register(self.instance._id, ClaimTypeIdNotExist())
        super().custom.register(self.instance, PermissionClaimTypeNotRemovable())
        super().validate()
