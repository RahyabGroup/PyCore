from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_edit_container import \
    ResourceEditContainer
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceEditContainer)
class ResourceEdit:
    _id = None
    name = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource._id = self._id
        resource.Name = self.name
        resource.edit()
        return "Done"
