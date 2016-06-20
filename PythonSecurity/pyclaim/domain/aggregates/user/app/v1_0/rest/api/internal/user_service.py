from flask import request
from pyfacil.web.rest.flask.response import *

from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.claime_type_removed_user import ClaimTypeRemovedUser
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.password_change import PasswordChange
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.register import Register
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.request_user_claim_add_by_claim_type_name import RequestUserClaimAddByClaimTypeName
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.request_user_claim_edit_by_claim_type_name_and_value import RequestUserClaimEditByClaimTypeNameAndValue
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.request_user_claim_remove_by_claim_type_name_and_value import RequestUserClaimRemoveByClaimTypeNameAndValue
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.resource_changed_user import ResourceChangedUser
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.internal.resource_removed_user import ResourceRemovedUser
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.password_remember import PasswordRemember
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.request_user_claim_get_by_claim_type_name import RequestUserClaimGetByClaimTypeName
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.request_user_get_by_user_name import RequestUserGetByUserName
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.request_user_get_by_user_name_and_password import \
    RequestUserGetByUserNameAndPassword
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.internal.request_user_get_by_id import RequestUserGetById
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserInfoCodes
from pyclaim.domain.aggregates.user.app.v1_0.rest import apis

__author__ = 'H.Rouhani'


@apis.route('/internal/users/get_by_user_name_password', methods=['GET'])
def request_user_get_by_user_name_and_password():
    dto = request.get_json()
    request_user_get_by_user_name_and_password_reader = RequestUserGetByUserNameAndPassword(dto)
    result = request_user_get_by_user_name_and_password_reader.execute()
    return ok(result)


@apis.route('/internal/users/get_by_user_name', methods=['GET'])
def request_user_get_by_user_name():
    dto = request.get_json()
    request_user_get_by_user_name_reader = RequestUserGetByUserName(dto)
    result = request_user_get_by_user_name_reader.execute()
    return ok(result)


@apis.route('/internal/users/<user_id>', methods=['GET'])
def request_user_get_by_id(user_id):
    dto = {"user_id": user_id}
    request_user_get_by_id_reader = RequestUserGetById(dto)
    result = request_user_get_by_id_reader.execute()
    return ok(result)

# todo : refactor: remove services and move func calls to relevant places
#
# @apis.route('/internal/user/<user_id>/claims/add_by_claim_type_name', methods=['PATCH'])
# def request_user_claim_add_by_claim_type_name(user_id):
#     dto = request.get_json()
#     dto["user_id"] = user_id
#     request_user_claim_add_by_claim_type_name_command = RequestUserClaimAddByClaimTypeName(dto)
#     request_user_claim_add_by_claim_type_name_command.execute()
#     return ok(None, UserInfoCodes.DONE)
#
#
# @apis.route('/internal/user/<user_id>/claims/edit_by_claim_type_name_and_value', methods=['PATCH'])
# def request_user_claim_edit_by_claim_type_name_and_value(user_id):
#     dto = request.get_json()
#     dto["user_id"] = user_id
#     request_user_claim_edit_by_claim_type_name_and_value_command = RequestUserClaimEditByClaimTypeNameAndValue(dto)
#     request_user_claim_edit_by_claim_type_name_and_value_command.execute()
#     return ok(None, UserInfoCodes.DONE)
#
#
# @apis.route('/internal/user/<user_id>/claims/remove_by_claim_type_name_and_value', methods=['PATCH'])
# def request_user_claim_remove_by_claim_type_name_and_value(user_id):
#     dto = request.get_json()
#     dto["user_id"] = user_id
#     request_user_claim_remove_by_claim_type_name_and_value_command = RequestUserClaimRemoveByClaimTypeNameAndValue(dto)
#     request_user_claim_remove_by_claim_type_name_and_value_command.execute()
#     return ok(None, UserInfoCodes.DONE)
#
#
# @apis.route('/internal/user/<user_id>/claims/get_by_claim_type_name', methods=['GET'])
# def request_user_claim_get_by_claim_type_name(user_id):
#     query_string = request.args
#     dto = {"user_id": user_id, "query_string": query_string}
#     request_user_claim_get_by_claim_type_name_query = RequestUserClaimGetByClaimTypeName(dto)
#     result = request_user_claim_get_by_claim_type_name_query.execute()
#     return ok(result)
#
#
# @apis.route('/internal/users/claims/resources', methods=['PUT'])
# def subscribe_resource_changed_user():
#     dto = request.get_json()
#     resource_changed_user_command = ResourceChangedUser(dto)
#     resource_changed_user_command.execute()
#     return ok(UserInfoCodes.DONE)
#
#
# @apis.route('/internal/users/claims/resources', methods=['DELETE'])
# def subscribe_resource_removed_user():
#     dto = request.get_json()
#     resource_removed_user_command = ResourceRemovedUser(dto)
#     resource_removed_user_command.execute()
#     return ok(UserInfoCodes.DONE)
#
#
# @apis.route('/internal/users/claims/claim_types/<claim_type_id>', methods=['DELETE'])
# def subscribe_claim_type_removed_user(claim_type_id):
#     dto = {"claim_type_id": claim_type_id}
#     claim_type_removed_user_command = ClaimTypeRemovedUser(dto)
#     claim_type_removed_user_command.execute()
#     return ok(UserInfoCodes.DONE)


@apis.route('/internal/register', methods=['POST'])
def request_register():
    dto = request.get_json()
    register_command = Register(dto)
    result = register_command.execute()
    response = created(result['user_id'])
    response.headers['token'] = result['token']
    return response


@apis.route('/internal/users/<user_id>/password_change', methods=['PUT'])
def request_password_change(user_id):
    dto = request.get_json()
    dto["user_id"] = user_id
    password_change_command = PasswordChange(dto)
    password_change_command.execute()
    return ok(UserInfoCodes.DONE)


@apis.route('/internal/users/password_remember', methods=['GET'])
def request_password_remember():
    query_string = request.args
    dto = {"query_string": query_string}
    remember_command = PasswordRemember(dto)
    result = remember_command.execute()
    return ok(result)
