from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.resource import ClaimTypeErrorCodes

from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

__author__ = 'Hooman'


class PermissionClaimTypeNotRemovable(Validation):
    def validate(self, claim_type_id):
        claim_type = ClaimType.get_by_id(claim_type_id)
        if claim_type.name == "PERMISSION":
            super().custom.manual(ClaimTypeErrorCodes.PERMISSION_CLAIM_TYPE_IS_NOT_REMOVABLE)
