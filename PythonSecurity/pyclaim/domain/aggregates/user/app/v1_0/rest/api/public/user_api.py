from flask import request
from pyfacil.web.rest.flask.response import *

from pyclaim.domain.aggregates.user.app.v1_0.rest import apis
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_claim_create import UserClaimCreate
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_claim_remove import UserClaimRemove
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_create import UserCreate
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_edit import UserEdit
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_remove import UserRemove
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.user_claim_edit import UserClaimEdit
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.public.user_get_all import UserGetAll
from pyclaim.domain.aggregates.user.app.v1_0.rest.query.public.user_get_by_id import UserGetById
from pyclaim.domain.aggregates.user.app.v1_0.rest.resource import UserInfoCodes
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.login import Login
from pyclaim.domain.aggregates.user.app.v1_0.rest.command.public.logout import Logout
from pyclaim.main.assembler import auth

__author__ = 'H.Rouhani'


@apis.route('/users', methods=['GET'])
@auth.authorize()
def user_get_all():
    user_get_all_reader = UserGetAll()
    result = user_get_all_reader.execute()
    return ok(result)


@apis.route('/users/<user_id>', methods=['GET'])
@auth.login_required()
def user_get_by_id(user_id):
    dto = {"user_id": user_id}
    user_get_by_id_reader = UserGetById(dto)
    result = user_get_by_id_reader.execute()
    return ok(result)


@apis.route('/users', methods=['POST'])
@auth.authorize()
def user_create():
    dto = request.get_json()
    user_create_command = UserCreate(dto)
    result = user_create_command.execute()
    return created(result)


@apis.route('/users', methods=['PUT'])
@auth.authorize()
def user_edit():
    dto = request.get_json()
    user_edit_command = UserEdit(dto)
    user_edit_command.execute()
    return ok(UserInfoCodes.DONE)


@apis.route('/users/<user_id>', methods=['DELETE'])
@auth.authorize()
def user_remove(user_id):
    dto = {"_id": user_id}
    user_remove_command = UserRemove(dto)
    user_remove_command.execute()
    return ok(UserInfoCodes.DONE)


@apis.route('/users/<user_id>/claims', methods=['POST'])
@auth.authorize()
def user_claim_create(user_id):
    dto = request.get_json()
    dto["_id"] = user_id
    user_claim_create_command = UserClaimCreate(dto)
    result = user_claim_create_command.execute()
    return created(result)


@apis.route('/users/<user_id>/claims/<claim_id>', methods=['PUT'])
@auth.authorize()
def user_claim_edit(user_id, claim_id):
    dto = request.get_json()
    dto["_id"] = user_id
    dto["claimId"] = claim_id
    user_claim_edit_command = UserClaimEdit(dto)
    user_claim_edit_command.execute()
    return ok(UserInfoCodes.DONE)


@apis.route('/users/<user_id>/claims/<claim_id>/', methods=['DELETE'])
@auth.authorize()
def user_claim_remove(user_id, claim_id):
    dto = {"_id": user_id, "claimId": claim_id}
    user_claim_remove_command = UserClaimRemove(dto)
    user_claim_remove_command.execute()
    return ok(UserInfoCodes.DONE)


@apis.route('/login', methods=['POST'])
def login():
    dto = request.get_json()
    login_command = Login(dto)
    result = login_command.execute()
    response = created(result['user_id'])
    response.headers['token'] = result['token']
    return response


@apis.route('/logout', methods=['DELETE'])
def logout():
    token = request.headers.get('token')
    logout_command = Logout(token)
    logout_command.execute()
    response = ok(UserInfoCodes.DONE)
    response.headers['token'] = ""
    return response



