import unittest
from pyvalidate.exception.validation_exception import ValidationException

from testpyvalidate.entity_helper.address import Address
from testpyvalidate.entity_helper.employee import Employee
from testpyvalidate.validation_helper.employee_validation import EmployeeValidation

__author__ = 'h.rouhani'


class TestList(unittest.TestCase):
    def test_CustomValidation_ShouldValidateItemsInListBasedOnSpecifiedValidationInstance(self):
        try:
            employee = Employee()
            employee.Name = "Hooman"
            employee.Office.Code = 11
            employee.Office.UnitNumber = 15
            employee.Office.FloorNo = -10
            employee.Office.SectionNo = 55

            address1 = Address()
            address1.Email = "hooman.frgmail.com"
            address1.Street = "Pasdaran"

            address2 = Address()
            address2.Email = "hooman.fryahoo.com"
            address2.Street = "golestan dovom pelake panjaho haft zange dovom"

            address3 = Address()
            address3.Email = "hooman.frhotmail.com"
            address3.Street = "pelak"

            employee.Phones.append(-1235)
            employee.Phones.append(-867)
            employee.Phones.append(0)

            employee.Addresses.append(address1)
            employee.Addresses.append(address2)
            employee.Addresses.append(address3)

            employeeValidation = EmployeeValidation()

            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldGuranteeValueShouldNotBeLowerThanMinValue(self):
        try:
            employee = Employee()
            employee.Name = "Hooman"
            employee.Office.Code = -1
            employee.Office.UnitNumber = -100
            employee.Office.FloorNo = 10
            employee.Office.SectionNo = 5
            employeeValidation = EmployeeValidation()
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldGuranteeValueShouldNotBeHigherThanMaxValue(self):
        try:
            employee = Employee()
            employee.Name = "Hooman"
            employee.Office.Code = -1
            employee.Office.UnitNumber = -100
            employee.Office.FloorNo = 10
            employee.Office.SectionNo = 5
            employee.Addresses.append(Address._getAddressInstance())
            employee.Addresses.append(Address._getAddressInstance())
            employee.Addresses.append(Address._getAddressInstance())
            employeeValidation = EmployeeValidation()
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldAcceptValueWhichIsAvailableInMaxMinBoundry(self):
        employee = Employee()
        employee.Name = "Hooman"
        employee.Office.Code = -1
        employee.Office.UnitNumber = -100
        employee.Office.FloorNo = 10
        employee.Office.SectionNo = 5
        employee.Addresses.append(Address._getAddressInstance())
        employee.Addresses.append(Address._getAddressInstance())
        employeeValidation = EmployeeValidation()
        result = employeeValidation.validate(employee)
        assert result is None
