from random import randint
from flask.ext.bcrypt import Bcrypt
from pyclaim.domain.aggregates.user.model.claim import Claim
from pyclaim.domain.aggregates.user.app.v1_0.rest.assembler import user_writer, user_reader

__author__ = 'Hooman'


class User:
    _id = None
    user_name = None
    password = None
    claims = None

    def __init__(self):
        self.claims = []

    def create(self):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

        user_name_claim_type = ClaimType.get_by_name("USER_NAME")

        user_default_claim = Claim()
        user_default_claim.claim_type_id = user_name_claim_type._id
        user_default_claim.value = self.user_name

        self.claims.append(user_default_claim)
        bcrypt = Bcrypt(None)
        password_hash = bcrypt.generate_password_hash(self.password)
        self.password = password_hash
        user_writer.create(self)

    def edit(self):
        bcrypt = Bcrypt(None)
        password_hash = bcrypt.generate_password_hash(self.password)
        self.password = password_hash
        user_writer.edit_main_info(self)

    def remove(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        user_writer.delete(self._id)
        Token.remove_by_user_id(self._id)

    def claim_add(self, claim):
        user_writer.claim_add(self._id, claim)

    def claim_edit(self, claim):
        user_writer.claim_edit(self._id, claim)

    def claim_remove(self, claim_id):
        user_writer.claim_remove(self._id, claim_id)

    def claim_add_by_claim_type_name(self, claim_type_name, claim_value):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        claim_type = ClaimType.get_by_name(claim_type_name)
        claim = Claim()
        claim.claim_type_id = claim_type._id
        claim.value = claim_value
        self.claim_add(claim)

    def claim_remove_by_claim_type_name_with_value(self, claim_type_name, claim_value):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        claim_type = ClaimType.get_by_name(claim_type_name)
        user_writer.claim_remove_by_claim_type_name_with_value(self._id, claim_type._id, claim_value)

    def claim_edit_by_claim_type_name_with_value(self, claim_type_name, claim_old_value, claim_value):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        claim_type = ClaimType.get_by_name(claim_type_name)
        user_writer.claim_edit_by_claim_type_name_with_value(self._id, claim_type._id, claim_old_value, claim_value)

    def claims_get_by_claim_type_name(self, claim_type_name):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        claim_type = ClaimType.get_by_name(claim_type_name)
        return user_reader.claims_get_claim_type_id(self._id, claim_type._id)

    def is_sys_admin(self):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType
        sys_admin_claim_type = ClaimType.get_role()
        for claim in self.claims:
            if claim.claim_type_id == sys_admin_claim_type._id and claim.value == "SYSADMIN":
                return True
        return False

    def password_change(self, new_password):
        from pyclaim.domain.aggregates.token.model.token import Token
        self.user_name = user_reader.user_name_get_by_id(self._id)
        bcrypt = Bcrypt(None)
        password_hash = bcrypt.generate_password_hash(new_password)
        self.password = password_hash
        user_writer.password_change(self._id, password_hash)
        Token.remove_by_user_id(self._id)

    def claim_exist(self, claim_type_id, claim_value):
        return user_reader.claim_exist(self._id, claim_type_id, claim_value)

    def claim_id_exist(self, claim_id):
        return user_reader.claim_id_exist(self._id, claim_id)

    def password_exist(self, password):
        bcrypt = Bcrypt(None)
        user = user_reader.get_by_id(self._id)
        return bcrypt.check_password_hash(user.password, password)

    @staticmethod
    def get_all():
        return user_reader.get_all()

    @staticmethod
    def get_by_id(user_id):
        return user_reader.get_by_id(user_id)

    @staticmethod
    def claim_remove_by_claim_type(claim_type_id):
        user_writer.claim_remove_by_claim_type(claim_type_id)

    @staticmethod
    def claim_remove_by_value(value):
        user_writer.claim_remove_by_value(value)

    @staticmethod
    def get_by_user_name(user_user_name):
        return user_reader.get_by_user_name(user_user_name)

    @staticmethod
    def get_main_info(user_id):
        return user_reader.get_main_info(user_id)

    @staticmethod
    def id_exists(user_id):
        return user_reader.exist_id(user_id)

    @staticmethod
    def exist_with_user_name(user_name):
        return user_reader.exist_with_user_name(user_name)

    @staticmethod
    def get_by_user_name_and_password(user_name, password):
        bcrypt = Bcrypt(None)
        user = user_reader.get_by_user_name(user_name)
        if user:
            if bcrypt.check_password_hash(user.password, password):
                return user
        return None

    @staticmethod
    def claim_update_value_by_new_value(resource_old_name, resource_new_name):
        user_writer.claim_update_value_by_new_value(resource_old_name, resource_new_name)

    @staticmethod
    def password_remember(user_name):
        from pyclaim.domain.aggregates.token.model.token import Token
        user = User.get_by_user_name(user_name)
        new_password = str(randint(10000000, 99999999))
        bcrypt = Bcrypt(None)
        password_hash = bcrypt.generate_password_hash(new_password)
        user.password = new_password
        user_writer.password_change(user._id, password_hash)
        Token.remove_by_user_id(user._id)
        return user


