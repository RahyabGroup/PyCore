from pystatic.main.config import Config

__author__ = 'azh'


class Url:
    VERSION_PATH = "/api/v1.0"
    DOMAIN_ADDRESS = "{}{}".format("http://localhost:8083", VERSION_PATH)
    SECURITY_DOMAIN_ADDRESS = Config().security_url

    SECURITY_DOMAIN_USER_CREATE_ROUTE = "/users"
    SECURITY_DOMAIN_USER_ACTIVATE_ROUTE = "/users/{}/activate"
    SECURITY_DOMAIN_USER_DEACTIVATE_ROUTE = "/users/{}/deactivate"
    SECURITY_DOMAIN_REGISTER_ROUTE = "/register"
    SECURITY_DOMAIN_LOGIN_ROUTE = "/login"
    SECURITY_DOMAIN_LOGOUT_ROUTE = "/logout"

    FILE_DOWNLOAD_ROUTE = '/files/{}/{}'
    FILE_UPLOAD_ROUTE = '/files/{}'

    APK_DOWNLOAD_ROUTE = '/apks/{}/{}'
    APK_DOWNLOAD_BY_VERSION_ID_ROUTE = '/apks/{}/download_by_version_id'
    APK_UPLOAD_ROUTE = '/apks/{}'

