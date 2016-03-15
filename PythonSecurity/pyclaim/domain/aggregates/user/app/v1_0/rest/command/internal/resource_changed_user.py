from pyclaim.domain.aggregates.user.model.user import User

__author__ = 'Hooman'


class ResourceChangedUser:
    resource_old_name = None
    resource_new_name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        User.claim_update_value_by_new_value(self.resource_old_name, self.resource_new_name)
        return "Done"