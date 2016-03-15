from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.user_full_detail import UserFullDetail
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class RequestUserGetById:
    user_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.get_by_id(self.user_id)
        user_full_detail = None
        if user:
            user_full_detail = UserFullDetail.create_from_user(user)
        return user_full_detail