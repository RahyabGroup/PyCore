from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.model.validation.resource_id_not_exist import ResourceIdNotExist

__author__ = 'Hooman'


class ResourceRemoveContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance._id, ResourceIdNotExist())
        super().string.size(self.instance._id, 3)
        super().validate()
