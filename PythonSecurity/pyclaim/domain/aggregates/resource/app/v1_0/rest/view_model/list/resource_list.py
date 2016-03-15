__author__ = 'H.Rouhani'


class ResourceList:
    _id = None
    name = None

    @staticmethod
    def create_from_resources(resources):
        result = []
        if resources:
            for resource in resources:
                resource_list = ResourceList()
                resource_list._id = resource._id
                resource_list.name = resource.name
                result.append(resource_list)
        return result