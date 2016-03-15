from pyclaim.domain.services.login import Login

__author__ = 'H.Rouhani'


class Register:
    user_name = None
    password = None

    def execute(self):
        from pyclaim.domain.aggregates.user.model.user import User
        user = User()
        user.user_name = self.user_name.lower()
        user.password = self.password
        user.create()
        login_service = Login()
        login_service.user_name = self.user_name
        login_service.password = self.password
        return login_service.execute()
