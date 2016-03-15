from pyvalidate.integer.positive import Positive
from pyvalidate.validation import Validation
from testpyvalidate.validation_helper.address_validation import AddressValidation
from testpyvalidate.validation_helper.office_validation import OfficeValidation

__author__ = 'Hooman'


class EmployeeValidation(Validation):
    def validate(self, employee):
        super().string.size(employee.Name, 3, 15, True)
        super().list.size(employee.addresses, 1, 2)
        super().list.custom(employee.Addresses, AddressValidation())
        super().list.custom(employee.Phones, Positive(False))
        super().custom.register(employee.office, OfficeValidation())
        return super().validate()
