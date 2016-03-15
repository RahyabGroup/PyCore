from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.user_detail import UserDetail
from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'H.Rouhani'


class RequestUserGetByUserName:
    user_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.get_by_user_name(self.user_name.lower())
        user_detail = None
        if user:
            user_detail = UserDetail.create_from_user(user, include_password=True)
        return user_detail