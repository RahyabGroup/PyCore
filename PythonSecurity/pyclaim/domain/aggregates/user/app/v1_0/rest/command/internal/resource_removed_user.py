from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class ResourceRemovedUser:
    resource_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        User.claim_remove_by_value(self.resource_name)
        return "Done"
