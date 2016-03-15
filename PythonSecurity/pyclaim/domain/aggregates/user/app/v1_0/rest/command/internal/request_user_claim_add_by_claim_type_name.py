from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class RequestUserClaimAddByClaimTypeName:
    user_id = None
    claim_type_name = None
    claim_value = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User()
        user._id = self.user_id
        user.claim_add_by_claim_type_name(self.claim_type_name, self.claim_value)
