__author__ = 'Hooman'


class ClaimDetail:
    _id = None
    claim_type_name = None
    claim_type_id = None
    value = None

    @staticmethod
    def create_from_claim(claim):
        if claim:
            claim_detail = ClaimDetail()
            claim_detail._id = claim._id
            claim_detail.value = claim.value
            claim_detail.claim_type_id = claim.claim_type_id
            claim_detail.claim_type_name = claim.claim_type_get().name
            return claim_detail
        return None

    @staticmethod
    def create_from_claims(claims):
        result = []
        if claims:
            for claim in claims:
                result.append(ClaimDetail.create_from_claim(claim))
        return result
