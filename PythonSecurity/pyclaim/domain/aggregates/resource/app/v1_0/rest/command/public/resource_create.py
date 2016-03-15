from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_create_container import \
    ResourceCreateContainer
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceCreateContainer)
class ResourceCreate:
    name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource.name = self.name
        resource.create()
        return resource._id
