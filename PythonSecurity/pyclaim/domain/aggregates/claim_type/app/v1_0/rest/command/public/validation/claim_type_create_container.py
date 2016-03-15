from pyvalidate.validation import Validation
from pyclaim.domain.aggregates.claim_type.model.validation.claim_type_name_exist import ClaimTypeNameExist

__author__ = 'Hooman'


class ClaimTypeCreateContainer(Validation):
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def execute(self):
        super().string.size(self.instance.name, 3)
        super().custom.register(self.instance.name, ClaimTypeNameExist())
        super().validate()
