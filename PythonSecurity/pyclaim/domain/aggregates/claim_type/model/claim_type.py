from pyclaim.domain.aggregates.claim_type.app.v1_0.rest.assembler import claim_type_reader, claim_type_writer

__author__ = 'Hooman'


class ClaimType:
    _id = None
    name = None

    def create(self):
        claim_type_writer.create(self)

    def remove(self):
        from pyclaim.domain.aggregates.resource.model.resource import Resource
        from pyclaim.domain.aggregates.user.model.user import User
        claim_type_writer.delete(self._id)
        #todo: caution = eventual consistency rules in ddd violated we must call them by using messaging patterns - hooman
        User.claim_remove_by_claim_type(self._id)
        Resource.claim_remove_by_claim_type(self._id)

    @staticmethod
    def get_role():
        return claim_type_reader.get_by_name('ROLE')

    @staticmethod
    def get_permission():
        return claim_type_reader.get_by_name('PERMISSION')

    @staticmethod
    def get_by_id(claim_type_id):
        return claim_type_reader.get_by_id(claim_type_id)

    @staticmethod
    def get_by_name(claim_type_name):
        return claim_type_reader.get_by_name(claim_type_name)

    @staticmethod
    def get_all():
        return claim_type_reader.get_all()

    @staticmethod
    def id_exists(claim_type_id):
        return claim_type_reader.exist_id(claim_type_id)

    @staticmethod
    def name_exists(claim_type_name):
        return claim_type_reader.exist_name(claim_type_name)