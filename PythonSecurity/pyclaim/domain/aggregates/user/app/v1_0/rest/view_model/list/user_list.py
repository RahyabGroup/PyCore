__author__ = 'Hooman'


class UserList:
    _id = None
    user_name = None

    @staticmethod
    def create_from_user(user_model):
        if user_model:
            user_list = UserList()
            user_list._id = user_model._id
            user_list.user_name = user_model.user_name
            return user_list
        return None

    @staticmethod
    def create_from_users(users):
        result = []
        if users:
            for user in users:
                result.append(UserList.create_from_user(user))
        return result
