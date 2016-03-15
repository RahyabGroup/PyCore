from flask import request
from pyfacil.web.rest.flask.response import *
from pyclaim.domain.aggregates.resource.app.v1_0.rest import apis
from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceInfoCodes
from pyclaim.main.assembler import auth

__author__ = 'H.Rouhani'

from pyclaim.domain.aggregates.resource.app.v1_0.rest.query.public.resource_get_all import ResourceGetAll
from pyclaim.domain.aggregates.resource.app.v1_0.rest.query.public.resource_get_by_id import ResourceGetById

from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_create import ResourceCreate
from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_claim_create import ResourceClaimCreate
from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_edit import ResourceEdit
from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_claim_edit import ResourceClaimEdit
from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_remove import ResourceRemove
from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.resource_claim_remove import ResourceClaimRemove


@apis.route('/resources', methods=['GET'])
@auth.authorize()
def resource_get_all():
    resource_get_all_reader = ResourceGetAll()
    result = resource_get_all_reader.execute()
    return ok(result)


@apis.route('/resources/<resource_id>', methods=['GET'])
@auth.authorize()
def resource_get_by_id(resource_id):
    dto = {"resource_id": resource_id}
    resource_get_by_id_reader = ResourceGetById(dto)
    result = resource_get_by_id_reader.execute()
    return ok(result)


@apis.route('/resources', methods=['POST'])
@auth.authorize()
def resource_create():
    dto = request.get_json()
    resource_create_command = ResourceCreate(dto)
    result = resource_create_command.execute()
    return created(result)


@apis.route('/resources/<resource_id>', methods=['PUT'])
@auth.authorize()
def resource_edit(resource_id):
    dto = request.get_json()
    dto["_id"] = resource_id
    resource_edit_command = ResourceEdit(dto)
    resource_edit_command.execute()
    return ok(ResourceInfoCodes.DONE)


@apis.route('/resources/<resource_id>', methods=['DELETE'])
@auth.authorize()
def resource_remove(resource_id):
    dto = {"_id": resource_id}
    resource_remove_command = ResourceRemove(dto)
    resource_remove_command.execute()
    return ok(ResourceInfoCodes.DONE)


@apis.route('/resources/<resource_id>/claims', methods=['POST'])
@auth.authorize()
def resource_claim_create(resource_id):
    dto = request.get_json()
    dto["_id"] = resource_id
    resource_claim_create_command = ResourceClaimCreate(dto)
    result = resource_claim_create_command.execute()
    return created(result)


@apis.route('/resources/<resource_id>/claims/<claim_id>', methods=['PUT'])
@auth.authorize()
def resource_claim_edit(resource_id, claim_id):
    dto = request.get_json()
    dto["_id"] = resource_id
    dto["claimId"] = claim_id
    resource_claim_edit_command = ResourceClaimEdit(dto)
    resource_claim_edit_command.execute()
    return ok(ResourceInfoCodes.DONE)


@apis.route('/resources/<resource_id>/claims/<claim_id>/', methods=['DELETE'])
@auth.authorize()
def resource_claim_remove(resource_id, claim_id):
    dto = {"_id": resource_id, "claimId": claim_id}
    resource_claim_remove_command = ResourceClaimRemove(dto)
    resource_claim_remove_command.execute()
    return ok(ResourceInfoCodes.DONE)
