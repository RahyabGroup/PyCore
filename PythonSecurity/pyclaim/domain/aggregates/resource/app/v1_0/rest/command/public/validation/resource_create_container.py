from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.model.validation.resource_name_exist import ResourceNameExist

__author__ = 'Hooman'


class ResourceCreateContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.name, 3)
        super().custom.register(self.instance.name, ResourceNameExist())
        super().validate()
