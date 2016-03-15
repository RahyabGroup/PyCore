from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.resource.app.v1_0.rest.resource import ResourceErrorCodes

from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ResourceIdNotExist(Validation):
    def validate(self, _id):
        is_available_id = Resource.id_exists(_id)
        if not is_available_id:
            super().custom.manual(ResourceErrorCodes.RESOURCE_ID_NOT_EXIST)
