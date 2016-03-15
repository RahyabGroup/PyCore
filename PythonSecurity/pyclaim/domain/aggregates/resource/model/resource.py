from pyclaim.domain.aggregates.resource.app.v1_0.rest.assembler import resource_reader, resource_writer
from pyclaim.domain.aggregates.resource.model.claim import Claim

__author__ = 'Hooman'


class Resource:
    _id = None
    name = None
    claims = None

    def __init__(self):
        self.claims = []

    def create(self):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        resource = Resource()
        permission_claim_type = ClaimType.get_permission()
        resource_default_claim = Claim()
        resource_default_claim.claim_type_id = permission_claim_type._id
        resource_default_claim.value = self.name
        resource.claims.append(resource_default_claim)
        resource_writer.create(self)

    def edit(self):
        resource_writer.edit_main_info(self)

    def remove(self):
        from pyclaim.domain.aggregates.user.model.user import User
        resource = resource_reader.get_main_info(self._id)
        resource_writer.delete(resource._id)
        User.claim_remove_by_value(resource.name)

    def claim_add(self, claim):
        resource_writer.claim_add(self._id, claim)

    def claim_edit(self, claim):
        resource_writer.claim_edit(self._id, claim)

    def claim_remove(self, claim_id):
        resource_writer.claim_remove(self._id, claim_id)

    def claim_exists(self, claim_type_id, claim_value):
        return resource_reader.claim_exist(self._id, claim_type_id, claim_value)

    def claim_id_exists(self, claim_id):
        return resource_reader.claim_id_exist(self._id, claim_id)

    def claim_is_of_claim_type(self, claim_id, claim_type_id):
        return resource_reader.claim_is_of_claim_type(self._id, claim_id, claim_type_id)

    @staticmethod
    def claim_remove_by_claim_type(claim_type_id):
        resource_writer.claim_remove_by_claim_type(claim_type_id)

    @staticmethod
    def get_by_name(resource_name):
        return resource_reader.get_by_name(resource_name)

    @staticmethod
    def get_all():
        return resource_reader.get_all()

    @staticmethod
    def get_by_id(resource_id):
        return resource_reader.get_by_id(resource_id)

    @staticmethod
    def id_exists(resource_id):
        return resource_reader.exist_id(resource_id)

    @staticmethod
    def name_exists(resource_name):
        return resource_reader.exist_name(resource_name)

