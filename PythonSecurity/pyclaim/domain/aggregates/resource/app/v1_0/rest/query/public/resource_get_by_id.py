from pyclaim.domain.aggregates.resource.app.v1_0.rest.view_model.detail.resource_detail import ResourceDetail
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ResourceGetById:
    resource_id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource.get_by_id(self.resource_id)
        resource_detail = ResourceDetail.create_from_resource(resource)
        return resource_detail
