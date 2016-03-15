from bson import ObjectId

__author__ = 'Hooman'


class Claim:
    value = None
    claim_type_id = None
    _id = None

    def __init__(self):
        self._id = str(ObjectId())

    def claim_type_get(self):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        return ClaimType.get_by_id(self.claim_type_id)
