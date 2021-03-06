import unittest

from pyvalidate.exception.validation_exception import ValidationException
from testpyvalidate.entity_helper.address import Address
from testpyvalidate.entity_helper.employee import Employee
from testpyvalidate.validation_helper.address_validation import AddressValidation
from testpyvalidate.validation_helper.employee_validation import EmployeeValidation
from testpyvalidate.validation_helper.english_employee_validation import EnglishEmployeeValidation
from testpyvalidate.validation_helper.persian_employee_validation import PersianEmployeeValidation

__author__ = 'h.rouhani'


class TestString(unittest.TestCase):
    def test_EmailValidation_ShouldNotAcceptIncorrectEmailAddress(self):
        address = Address()
        addressValidation = AddressValidation()

        try:

            address.Email = "hooman.frgmail.com"
            address.Street = "Pasdaran Golestane dovom"
            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

        try:
            address.Email = "hooman.fr@gmailcom"

            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_EmailValidation_ShouldAcceptCorrectEmailAddress(self):
        address = Address()
        addressValidation = AddressValidation()
        address.Email = "hooman.fr@gmail.com"
        address.Street = "Pasdaran Golestane dovom"
        result = addressValidation.validate(address)
        assert result is None

    def test_SizeValidation_ShouldGuranteeStringSizeShouldNotBeLowerThanMinValue(self):
        try:
            address = Address()
            addressValidation = AddressValidation()
            address.Email = "hooman.fr@gmail.com"
            address.Street = "Pasdaran"
            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldGuranteeStringSizeShouldNotBeHigherThanMaxValue(self):
        try:
            address = Address()
            addressValidation = AddressValidation()
            address.Email = "hooman.fr@gmail.com"
            address.Street = "Pasdaran golestane dovom pelake 57 zange 2"
            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_TextSizeValidation_ShouldAcceptTextWhichItsCountOfWordsIsAvailableInMaxMinBoundry(self):
        address = Address()
        addressValidation = AddressValidation()
        address.Email = "hooman.fr@gmail.com"
        address.Street = """alsdkfjasdk
lkdjfalkf
lkjdfalskfj
akjfdakjdf"""
        result = addressValidation.validate(address)
        assert result is None
        address.Street = "Pasdaran golestane dovom pelake panjahohaft"
        anotehrResult = addressValidation.validate(address)
        assert anotehrResult is None
        address.Street = "Pasdaran golestane dovom"
        andAnotehrResult = addressValidation.validate(address)
        assert andAnotehrResult is None

    def test_sizeValidation_ShouldAcceptTextWhichItsCountOfCharactersIsAvailableInMaxMinBoundry(self):
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
        try:
            employee.Name = "ho"
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_OnlyStringValidation_ShouldNotAcceptStringWhichContainsNotAlphabeticalCharacter(self):
        address = Address()
        addressValidation = AddressValidation()
        try:
            address.Email = "hooman.fr@gmail.com"
            address.Street = "?????? ????? ???? 2"
            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

        try:
            address.Street = "Pasdaran-golestane dovom"

            result = addressValidation.validate(address)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_OnlyStringValidation_ShouldAcceptStringWhichOnlyContainsAlphabeticalCharacterWithSpaces(self):
        address = Address()
        addressValidation = AddressValidation()
        address.Email = "hooman.fr@gmail.com"
        address.Street = "خیابان آزادي کوچه رها"
        addressValidation.validate(address)
        address.street = "azadi st raha ave"
        result = addressValidation.validate(address)
        assert result is None

    def test_OnlyEnglishValidation_ShouldNotAcceptNotEnglishString(self):
        employee = Employee()
        only_english_validation = EnglishEmployeeValidation()
        try:
            employee.Name = "آقایmr"
            result = only_english_validation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

        try:
            employee.Name = " رضوان"
            result = only_english_validation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_OnlyEnglishValidation_ShouldAcceptStringWhichOnlyContainsEnglishAlphabeticalCharacterWithSpaces(self):
        employee = Employee()
        employee.name = "Rezvan aj"
        only_english_validation = EnglishEmployeeValidation()
        result = only_english_validation.validate(employee)
        assert result is None

    def test_OnlyPersianValidation_ShouldNotAcceptNotPersianString(self):
        employee = Employee()
        only_persian_validation = PersianEmployeeValidation()
        try:
            employee.Name = "آقایmr"
            result = only_persian_validation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

        try:
            employee.Name = "mis aj"
            result = only_persian_validation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_OnlyPersianValidation_ShouldAcceptStringWhichOnlyContainsPersianAlphabeticalCharacterWithSpaces(self):
        employee = Employee()
        employee.name = "رضوان آژ"
        only_persian_validation = PersianEmployeeValidation()
        result = only_persian_validation.validate(employee)
        assert result is None

    def test_ObjectIdValidation_ShouldNotAcceptIncorrectObjectId(self):
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
        try:
            employee._id = "12345a"
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

        try:
            employee._id = "12zxh"
            result = employeeValidation.validate(employee)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_ObjectIdValidation_ShouldAcceptCorrectObjectId(self):
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
        try:
            employee._id = "58fafa353ae7282b18041c1e"
            result = employeeValidation.validate(employee)
            assert result is None
        except ValidationException as ex:
            assert ex.Errors