import os
from flask_bcrypt import Bcrypt
from pyfacil.web.rest.builder.flask.flask_app_builder import FlaskAppBuilder

from pyclaim.domain import aggregates
from pyclaim.main.config import Config

__author__ = 'H.Rouhani'

app_mode = os.environ.get('SECURITY_CFG_MODE', None)


def prepare_db():
    def create_claim_type(name):
        from pyclaim.domain.aggregates.claim_type.model.claim_type import ClaimType

        try:
            if not ClaimType.name_exists(name):
                claim_type = ClaimType()
                claim_type.name = name
                ClaimType.create(claim_type)
                return claim_type
        except Exception as ex:
            pass

    def create_sysadmin(role_claim_type):
        from pyclaim.domain.aggregates.user.model.user import User
        from pyclaim.domain.aggregates.user.model.claim import Claim
        from pyclaim.domain.aggregates.user.app.v1_0.rest.assembler import user_writer, user_reader

        try:
            user_id = "560121abcbf62c13d4567f0d"
            if not user_reader.exist_id(user_id):
                from pyclaim.domain.aggregates.user.model.status import Status
                sysadmin_user_name = "sysadmin@security.com"
                sysadmin = User()
                sysadmin._id = user_id
                sysadmin.user_name = sysadmin_user_name
                sysadmin.status = Status.activated
                bcrypt = Bcrypt(None)
                password_hash = bcrypt.generate_password_hash(sysadmin_user_name)
                sysadmin.password = password_hash
                sysadmin_claim = Claim()
                sysadmin_claim.claim_type_id = role_claim_type._id
                sysadmin_claim.value = "SYSADMIN"
                sysadmin.claims.append(sysadmin_claim)
                user_writer.create(sysadmin)

            super_user_id = "580e04a33ae7280ae09d93a5"
            if not user_reader.exist_id(super_user_id):
                from pyclaim.domain.aggregates.user.model.status import Status
                super_admin_user_name = "super_admin@motanaweb.com"
                super_admin = User()
                super_admin._id = user_id
                super_admin.user_name = super_admin_user_name
                super_admin.status = Status.activated
                bcrypt = Bcrypt(None)
                password_hash = bcrypt.generate_password_hash("M0t@n@w3b")
                super_admin.password = password_hash
                super_admin_claim = Claim()
                super_admin_claim.claim_type_id = role_claim_type._id
                super_admin_claim.value = "SYSADMIN"
                super_admin.claims.append(super_admin_claim)
                user_writer.create(super_admin)
        except Exception as ex:
            pass

    role_claim_type = create_claim_type("ROLE")
    create_claim_type("PERMISSION")
    create_claim_type("USER_NAME")
    create_claim_type("STATUS")
    create_sysadmin(role_claim_type)


if app_mode == "dev.cfg" or not app_mode:
    app = FlaskAppBuilder([aggregates], log_path=Config().log_path).construct()
    prepare_db()
    app.run(host="0.0.0.0", port=8081, threaded=True)
