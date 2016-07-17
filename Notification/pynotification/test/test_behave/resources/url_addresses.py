__author__ = 'azh'

from pynotification.main.config import Config


class Url:
    VERSION_PATH = "/api/v1.0"
    DOMAIN_ADDRESS = "{}{}".format("http://localhost:8084", VERSION_PATH)
    # SECURITY_DOMAIN_ADDRESS = Config().security_url
    # # IPN_DOMAIN_ADDRESS = config().IPN_MESSAGING_URL
    #
    # SECURITY_DOMAIN_USER_CREATE_ROUTE = "/users"
    # SECURITY_DOMAIN_USER_ACTIVATE_ROUTE = "/users/{}/activate"
    # SECURITY_DOMAIN_USER_DEACTIVATE_ROUTE = '/users/{}/deactivate'
    # SECURITY_DOMAIN_REGISTER_ROUTE = "/register"
    # SECURITY_DOMAIN_LOGIN_ROUTE = "/login"
    # SECURITY_DOMAIN_LOGOUT_ROUTE = "/logout"
    SECURITY_DOMAIN_ADDRESS = Config().security_url
    IPN_DOMAIN_ADDRESS = Config().ipn_url

    SECURITY_DOMAIN_USER_CREATE_ROUTE = "/users"
    SECURITY_DOMAIN_REGISTER_ROUTE = "/register"
    SECURITY_DOMAIN_LOGIN_ROUTE = "/login"
    SECURITY_DOMAIN_LOGOUT_ROUTE = "/logout"

    IPN_DOMAIN_PERSON_ACTIVATE_ROUTE = "/persons/{}/activate"
    IPN_DOMAIN_PERSON_DEACTIVATE_ROUTE = '/persons/{}/deactivate'
    IPN_DOMAIN_PERSON_GET_BY_ID_ROUTE = "/persons/{}"
    IPN_DOMAIN_BASIC_INFO_CREATE_ROUTE = "/persons/{}"
    IPN_DOMAIN_BASIC_INFO_EDIT_ROUTE = "/persons/{}"
    IPN_DOMAIN_COMPANY_TYPE_CREATE_ROUTE = '/company_types'
    IPN_DOMAIN_COMPANY_SIZE_CREATE_ROUTE = '/company_sizes'
    IPN_DOMAIN_COMPANY_INDUSTRY_CREATE_ROUTE = '/company_industries'
    IPN_DOMAIN_COMPANY_OPERATION_CREATE_ROUTE = '/company_operations'
    IPN_DOMAIN_PERSON_CREATE_ROUTE = "/persons"


    IPN_DOMAIN_PERSON_GET_BY_ID_ROUTE = "/persons/{}"
    IPN_DOMAIN_BASIC_INFO_CREATE_ROUTE = "/persons/{}"
    IPN_DOMAIN_BASIC_INFO_EDIT_ROUTE = "/persons/{}"
    IPN_DOMAIN_COMPANY_TYPE_CREATE_ROUTE = '/company_types'
    IPN_DOMAIN_COMPANY_SIZE_CREATE_ROUTE = '/company_sizes'
    IPN_DOMAIN_COMPANY_INDUSTRY_CREATE_ROUTE = '/company_industries'
    IPN_DOMAIN_COMPANY_OPERATION_CREATE_ROUTE = '/company_operations'

    PUSH_ROUTE = '/internal/notification'
    SUBSCRIBE_ROUTE = '/notification/{}/{}'
    NOTIFICATION_GET_BY_RECEIVER_ID_ROUTE = '/notification/receiver/{}/message_type/{}'      #'/notification/{}'
    NOTIFICATION_COUNT_GET_BY_RECEIVER_ID_ROUTE = '/notification/receiver/{}/message_type/{}/count'      #'/notification/{}/count'
    NOTIFICATION_MARK_AS_VIEWED_ROUTE = '/notification/{}'
    NOTIFICATION_SUBSCRIBE = '/notification/{}/{}'
