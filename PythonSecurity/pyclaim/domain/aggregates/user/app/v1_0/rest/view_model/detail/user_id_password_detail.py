__author__ = 'H.Rouhani'


class UserIdPasswordDetail:
    user_id = None
    password = None

    @staticmethod
    def create_from_user(user):
        if user:
            user_id_password_detail = UserIdPasswordDetail()
            user_id_password_detail.user_id = user._id
            user_id_password_detail.password = user.password
            return user_id_password_detail
        return None
