from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.view_model.detail.claim_type_detail import ClaimTypeDetail
from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

__author__ = 'Hooman'


class ClaimTypeGetAll:
    def execute(self):
        claim_types = ClaimType.get_all()
        claim_types_detail = ClaimTypeDetail.create_from_claim_types(claim_types)
        return claim_types_detail
