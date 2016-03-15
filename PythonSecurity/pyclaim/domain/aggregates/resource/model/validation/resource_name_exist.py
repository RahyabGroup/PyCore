from pyvalidate.validation import Validation

from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceErrorCodes
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ResourceNameExist(Validation):
    def validate(self, name):
        is_name_exist = Resource.name_exists(name)
        if is_name_exist:
            super().custom.manual(ResourceErrorCodes.RESOURCE_NAME_EXIST)
