import unittest
from pyvalidate.exception.validation_exception import ValidationException

from testpyvalidate.entity_helper.address import Address
from testpyvalidate.entity_helper.employee import Employee
from testpyvalidate.validation_helper.employee_validation import EmployeeValidation

__author__ = 'h.rouhani'


class TestObject(unittest.TestCase):
    def test_CustomValidation_ShouldReturnErrorForRegisteredCustomValidation(self):
        try:
            employee = Employee()
            employee.Name = "Hooman"
            employee.Office.Code = 0
            employee.Office.UnitNumber = 10
            employee.Office.FloorNo = -10
            employee.Office.SectionNo = 0
            employee.Addresses.append(Address._getAddressInstance())
            employee.Addresses.append(Address._getAddressInstance())
            employeeValidation = EmployeeValidation()
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_CustomValidation_ShouldAcceptDateWhichObserveCustomValidation(self):
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

    def test_ManualValidation_ShouldReturnValidationErrorWithSpecifiedCode(self):
        try:
            employee = Employee()
            employee.Name = "Hooman"
            employee.Office.Code = -1
            employee.Office.UnitNumber = -100
            employee.Office.FloorNo = 10
            employee.Office.SectionNo = 753
            employee.Addresses.append(Address._getAddressInstance())
            employee.Addresses.append(Address._getAddressInstance())
            employeeValidation = EmployeeValidation()
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_NullValidation_ShouldNotAcceptItemWithValueOfNone(self):
        try:
            employee = Employee()
            employee.Name = None
            employee.Office.Code = -1
            employee.Office.UnitNumber = -100
            employee.Office.FloorNo = 10
            employee.Office.SectionNo = 5
            employee.Addresses.append(Address._getAddressInstance())
            employee.Addresses.append(Address._getAddressInstance())
            employeeValidation = EmployeeValidation()
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors