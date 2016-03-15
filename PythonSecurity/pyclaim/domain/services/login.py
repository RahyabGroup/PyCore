from pyutil.cryptography.rsa.object_coder import ObjectCoder
from pyvalidate.exception.validation_exception import ValidationException

from pyclaim.main.config import Config
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserErrorCodes

__author__ = 'H.Rouhani'


class Login:
    user_name = None
    password = None

    def execute(self):
        from pyclaim.domain.aggregates.user.model.user import User
        from pyclaim.domain.aggregates.token.model.token import Token

        user = User.get_by_user_name_and_password(self.user_name, self.password)
        if user is None:
            result = UserErrorCodes.USER_NOT_AVAILABLE
            result["data"] = "user_name: %s" % self.user_name
            raise ValidationException([result])
        user_token = Token.generate(user._id)
        token = {"token_id": user_token.token_id,
                 "user_id": user_token.user_id,
                 "is_sys_admin": user.is_sys_admin()
                 }
        object_coder = ObjectCoder(Config().secret_key)
        hashed_token = object_coder.encode(token)
        login_info = {"token": hashed_token, "user_id": user._id}
        return login_info
