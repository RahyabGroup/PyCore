from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.validation.password_remember_container import \
    PasswordRememberContainer
from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.user_id_password_detail import UserIdPasswordDetail

from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.main.assembler import validator

__author__ = 'H.Rouhani'


@validator.validation(PasswordRememberContainer)
class PasswordRemember:
    query_string = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.password_remember(self.query_string["user_name"])
        user_id_password_detail = UserIdPasswordDetail.create_from_user(user)
        return user_id_password_detail
