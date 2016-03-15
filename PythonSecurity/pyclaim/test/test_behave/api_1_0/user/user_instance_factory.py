from bson import ObjectId

__author__ = 'ici'


# class User:
#     user_name = None
#     password = None
#
#     def __init__(self, user_name, password):
#         self.user_name = user_name
#         self.password = password

class UserInstanceFactory:
    # def create_user_instance(self, user_name, password):
    #     user1 = User()
    #     user1.user_name = user_name
    #     user1.password = password
    #     return user1

    def create_user_dict(self):
        dto = {"user_name": "{}@mailinator.com".format(str(ObjectId())), "password": str(ObjectId())}
        return dto

    # def create_user_dict_with_user_name(self, user_name):
    #     password = str(ObjectId())
    #     dto = {"user_name": user_name, "password": password}
    #     print(user_name, " ", password)
    #     return dto

    def create_user_dict_with_user_name_password(self, user_name, password):
        dto = {"user_name": user_name, "password": password}
        print(user_name, " ", password)
        return dto

    def create_login_dict(self, user_name, password):
        dto = {"user_name": user_name, "password": password}
        return dto
