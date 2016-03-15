from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class ClaimTypeRemovedUser:
    claim_type_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        User.claim_remove_by_claim_type(self.claim_type_id)
        return "Done"
