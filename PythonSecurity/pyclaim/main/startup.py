import os
from flask.ext.bcrypt import Bcrypt

from pyfacil.web.rest.builder.flask.flask_app_builder import FlaskAppBuilder

from pyclaim.domain import aggregates

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
                sysadmin_user_name = "sysadmin@security.com"
                sysadmin = User()
                sysadmin._id = user_id
                sysadmin.user_name = sysadmin_user_name
                bcrypt = Bcrypt(None)
                password_hash = bcrypt.generate_password_hash(sysadmin_user_name)
                sysadmin.password = password_hash
                sysadmin_claim = Claim()
                sysadmin_claim.claim_type_id = role_claim_type._id
                sysadmin_claim.value = "SYSADMIN"
                sysadmin.claims.append(sysadmin_claim)
                user_writer.create(sysadmin)
        except Exception as ex:
            pass

    role_claim_type = create_claim_type("ROLE")
    create_claim_type("PERMISSION")
    create_claim_type("USER_NAME")
    create_claim_type("STATUS")
    create_sysadmin(role_claim_type)


if app_mode == "dev.cfg" or not app_mode:
    app = FlaskAppBuilder([aggregates]).construct()
    prepare_db()
    app.run(host="localhost", port=8081, threaded=True)
