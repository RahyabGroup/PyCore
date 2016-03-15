from pyclaim.domain.aggregates.user.app.v1_0.rest.query.public.validation.user_get_by_id_container import UserGetByIdContainer
from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.detail.user_detail import UserDetail
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(UserGetByIdContainer)
class UserGetById:
    user_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        user = User.get_by_id(self.user_id)
        user_detail = UserDetail.create_from_user(user)
        return user_detail
