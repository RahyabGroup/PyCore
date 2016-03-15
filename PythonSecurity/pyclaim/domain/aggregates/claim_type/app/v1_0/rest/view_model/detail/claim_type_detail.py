__author__ = 'Hooman'


class ClaimTypeDetail:
    _id = None
    name = None

    @staticmethod
    def create_from_claim_type(claim_type):
        claim_type_detail = ClaimTypeDetail()
        claim_type_detail._id = claim_type._id
        claim_type_detail.name = claim_type.name
        return claim_type_detail

    @staticmethod
    def create_from_claim_types(claim_types):
        results = []
        if claim_types:
            for claim_type in claim_types:
                results.append(ClaimTypeDetail.create_from_claim_type(claim_type))
        return results