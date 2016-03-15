from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.claim_detail import ClaimDetail
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class RequestUserClaimGetByClaimTypeName:
    user_id = None
    query_string = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = self.user_id
        claims = user.claims_get_by_claim_type_name(self.query_string["claim_type_name"])
        claims_detail = ClaimDetail.create_from_claims(claims)
        return claims_detail
