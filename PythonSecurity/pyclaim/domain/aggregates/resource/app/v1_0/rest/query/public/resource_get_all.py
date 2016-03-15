from pyclaim.domain.aggregates.resource.app.v1_0.rest.view_model.list.resource_list import ResourceList
from pyclaim.domain.aggregates.resource.model.resource import Resource

__author__ = 'Hooman'


class ResourceGetAll:
    def execute(self):
        resources = Resource.get_all()
        resource_list = ResourceList.create_from_resources(resources)
        return resource_list
