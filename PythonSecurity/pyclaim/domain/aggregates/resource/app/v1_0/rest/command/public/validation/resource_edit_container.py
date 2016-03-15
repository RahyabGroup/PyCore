from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.model.validation.resource_id_not_exist import ResourceIdNotExist
from pyclaim.domain.aggregates.resource.model.validation.resource_name_exist import ResourceNameExist

__author__ = 'Hooman'


class ResourceEditContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().custom.register(self.instance._id, ResourceIdNotExist())
        super().custom.register(self.instance.name, ResourceNameExist())
        super().string.size(self.instance._id, 3)
        super().string.size(self.instance.name, 3)
        super().validate()
