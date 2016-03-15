from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.resource import ClaimTypeErrorCodes
from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

__author__ = 'Hooman'


class ClaimTypeNameExist(Validation):
    def validate(self, name):
        is_name_exist = ClaimType.name_exists(name)
        if is_name_exist:
            super().custom.manual(ClaimTypeErrorCodes.CLAIM_TYPE_NAME_EXIST)
