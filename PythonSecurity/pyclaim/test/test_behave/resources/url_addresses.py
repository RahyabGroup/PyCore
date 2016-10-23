from pyclaim.main.config import Config
__author__ = 'azh'


class Url:
    # VERSION_PATH = "/api/v1.0"
    # config = Config()
    DOMAIN_ADDRESS = Config().security_url   #  "{}{}".format("http://localhost:8081", VERSION_PATH)

    LOGIN_ROUTE = "/login"
    LOGOUT_ROUTE = "/logout"

    USER_CREATE_ROUTE = '/users'
    USER_EDIT_ROUTE = '/users'
    USER_GET_BY_ID_ROUTE = '/users/{}'
    USER_GET_ALL_ROUTE = '/users'
    USER_REMOVE_ROUTE = '/users/{}'
    USER_ACTIVATE_ROUTE = '/users/{}/activate'
    USER_DEACTIVATE_ROUTE = '/users/{}/deactivate'

    CLAIM_TYPE_GET_ALL_ROUTE = "/claim_types"
    CLAIM_TYPE_CREATE_ROUTE = "/claim_types"
    CLAIM_TYPE_REMOVE_ROUTE = "/claim_types/{}"

    REGISTER_ROUTE = "/internal/register"
    PASSWORD_REMEMBER_ROUTE = '/internal/users/password_remember'
    PASSWORD_CHANGE_ROUTE = '/internal/users/{}/password_change'
