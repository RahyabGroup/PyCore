from pyclaim.domain.services.authorize import Authorize

__author__ = 'H.Rouhani'


class RequestTokenAuthorize:
    token_id = None
    resource_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        authorize_service = Authorize()
        authorize_service.token_id = self.token_id
        authorize_service.resource_name = self.resource_name
        return authorize_service.execute()
