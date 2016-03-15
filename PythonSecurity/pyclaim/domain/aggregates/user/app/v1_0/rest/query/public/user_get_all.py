from pyclaim.domain.aggregates.user.model.user import User
from pyclaim.domain.aggregates.user.app.v1_0.rest.view_model.list.user_list import UserList

__author__ = 'Hooman'


class UserGetAll:
    def execute(self):
        users = User.get_all()
        users_list = UserList.create_from_users(users)
        return users_list
