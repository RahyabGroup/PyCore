


__author__ = 'H.Rouhani'


class Authorize:
    token_id = None
    resource_name = None

    def execute(self):
        from pyclaim.domain.aggregates.token.model.token import Token
        from pyclaim.domain.aggregates.user.model.user import User
        from pyclaim.domain.aggregates.resource.model.resource import Resource

        token = Token.get_by_id(self.token_id)

        if not token:
            return "Not Authenticated"

        user = User.get_by_id(token.user_id)

        if not user:
            return "Not Authenticated"

        if user.is_sys_admin():
            return "Authorized"

        resource = Resource.get_by_name(self.resource_name)

        if not resource:
            return "Not Authorized"

        for user_claim in user.claims:
            for resource_claim in resource.claims:
                if resource_claim["claim_type"]["_id"] == user_claim["claim_type"]["_id"] and resource_claim["value"] == user_claim["value"]:
                    return "Authorized"

        return "Not Authorized"
