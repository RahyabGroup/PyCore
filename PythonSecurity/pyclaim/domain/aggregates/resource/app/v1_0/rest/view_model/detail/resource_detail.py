from pyclaim.domain.aggregates.resource.app.v1_0.rest.view_model.detail.claim_detail import ClaimDetail

__author__ = 'Hooman'


class ResourceDetail:
    _id = None
    name = None

    @staticmethod
    def create_from_resource(resource):
        resource_detail = ResourceDetail()
        resource_detail._id = resource._id
        resource_detail.name = resource.name
        resource_detail.claims = ClaimDetail.create_from_claims(resource.Claims)
        return resource_detail

    @staticmethod
    def create_from_resources(resource):
        result = []
        if resource:
            for resource in resource:
                result.append(ResourceDetail.create_from_resource(resource))
        return result