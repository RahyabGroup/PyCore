from flask import request
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest import apis
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.command.public.claim_type_create import ClaimTypeCreate

from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.query.public.claim_type_get_all import ClaimTypeGetAll
from pyfacil.web.rest.flask.response import *
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.command.public.claim_type_remove import ClaimTypeRemove
from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.resource import ClaimTypeInfoCodes
from pyclaim.main.assembler import auth

__author__ = 'H.Rouhani'


@apis.route('/claim_types', methods=['GET'])
@auth.authorize()
def claim_type_get_all():
    claim_types_get_all_reader = ClaimTypeGetAll()
    results = claim_types_get_all_reader.execute()
    return ok(results)


@apis.route('/claim_types', methods=['POST'])
@auth.authorize()
def claim_type_create():
    dto = request.get_json()
    claim_type_create_command = ClaimTypeCreate(dto)
    result = claim_type_create_command.execute()
    return created(result)


@apis.route('/claim_types/<claim_type_id>', methods=['DELETE'])
@auth.authorize()
def claim_type_remove(claim_type_id):
    dto = {"_id": claim_type_id}
    claim_type_remove_command = ClaimTypeRemove(dto)
    claim_type_remove_command.execute()
    return ok(ClaimTypeInfoCodes.DONE)
