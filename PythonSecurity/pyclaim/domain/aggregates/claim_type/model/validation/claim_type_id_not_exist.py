from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.resource import ClaimTypeErrorCodes
from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

__author__ = 'Hooman'


class ClaimTypeIdNotExist(Validation):
    def validate(self, _id):
        is_available_id = ClaimType.id_exists(_id)
        if not is_available_id:
            super().custom.manual(ClaimTypeErrorCodes.CLAIM_TYPE_ID_NOT_EXIST)
