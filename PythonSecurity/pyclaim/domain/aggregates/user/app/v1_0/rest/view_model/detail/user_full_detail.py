from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.claim_detail import ClaimDetail

__author__ = 'H.Rouhani'


class UserFullDetail:
    _id = None
    user_name = None
    claims = None
    is_sys_admin = None

    def __init__(self):
        self.claims = []

    @staticmethod
    def create_from_user(user):
        if user:
            user_full_detail = UserFullDetail()
            user_full_detail._id = user._id
            user_full_detail.user_name = user.user_name
            user_full_detail.is_sys_admin = user.is_sys_admin()
            user_full_detail.claims = ClaimDetail.create_from_claims(user.claims)
            return user_full_detail
        return None