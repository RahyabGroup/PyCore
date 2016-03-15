from pyclaim.domain.aggregates.resource.app.v1_0.rest.command.public.validation.resource_remove_container import \
    ResourceRemoveContainer
from pyclaim.domain.aggregates.resource.model.resource import Resource
from pyclaim.main.assembler import validator

__author__ = 'Hooman'


@validator.validation(ResourceRemoveContainer)
class ResourceRemove:
    _id = None

    def __init__(self, dto):
        self.__dict__.update(dto)

    def execute(self):
        resource = Resource()
        resource._id = self._id
        resource.remove()
        return "Done"
