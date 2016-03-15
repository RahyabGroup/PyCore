from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.claim_detail import ClaimDetail

__author__ = 'Hooman'


class UserDetail:
    _id = None
    user_name = None
    claims = None
    password = None

    def __init__(self):
        self.claims = []

    @staticmethod
    def create_from_user(user, include_password=False):
        if user:
            user_detail = UserDetail()
            user_detail._id = user._id
            user_detail.user_name = user.user_name
            user_detail.claims = ClaimDetail.create_from_claims(user.claims)
            if include_password:
                user_detail.password = user.password
            return user_detail
        return None
