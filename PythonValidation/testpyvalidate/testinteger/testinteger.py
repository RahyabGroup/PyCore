import unittest
from pyvalidate.exception.validation_exception import ValidationException

from testpyvalidate.entity_helper.office import Office
from testpyvalidate.validation_helper.office_validation import OfficeValidation

__author__ = 'h.rouhani'

class TestInteger(unittest.TestCase):
    def test_NegativeValidation_ShouldGuaranteeTheValueIsNegative(self):
        try:
            office = Office()
            office.Code = 10
            office.UnitNumber = 5
            office.FloorNo = 10
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_NegativeValidation_ShouldReturnValidationErrorIfZeroIsNotIncluded(self):
        try:
            office = Office()
            office.Code = 0
            office.UnitNumber = -5
            office.FloorNo = 10
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_NegativeValidation_ShouldAcceptDataWithValueOfZeroIfZeroIsIncluded(self):
        office = Office()
        office.Code = -1
        office.UnitNumber = 0
        office.FloorNo = 10
        office.SectionNo = 5
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None

    def test_NegativeValidation_ShouldAcceptNegativeData(self):
        office = Office()
        office.Code = -1
        office.UnitNumber = -100
        office.FloorNo = 10
        office.SectionNo = 5
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None

    def test_PositiveValidation_ShouldGuaranteeTheValueIsPositive(self):
        try:
            office = Office()
            office.Code = -1
            office.UnitNumber = -100
            office.FloorNo = -50
            office.SectionNo = -10
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_PositiveValidation_ShouldReturnValidationErrorIfZeroIsNotIncluded(self):
        try:
            office = Office()
            office.Code = -1
            office.UnitNumber = -100
            office.FloorNo = 0
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_PositiveValidation_ShouldAcceptDataWithValueOfZeroIfZeroIsIncluded(self):
        office = Office()
        office.Code = -1
        office.UnitNumber = -100
        office.FloorNo = 10
        office.SectionNo = 0
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None

    def test_PositiveValidation_ShouldAcceptPositiveData(self):
        office = Office()
        office.Code = -1
        office.UnitNumber = -100
        office.FloorNo = 10
        office.SectionNo = 5
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None

    def test_SizeValidation_ShouldGuranteeValueShouldNotBeLowerThanMinValue(self):
        try:
            office = Office()
            office.Code = -1
            office.UnitNumber = -100
            office.FloorNo = 1
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldGuranteeValueShouldNotBeHigherThanMaxValue(self):
        try:
            office = Office()
            office.Code = -1
            office.UnitNumber = -100
            office.FloorNo = 16
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors

    def test_SizeValidation_ShouldAcceptValueWhichIsAvailableInMaxMinBoundry(self):
        office = Office()
        office.Code = -1
        office.UnitNumber = -100
        office.FloorNo = 10
        office.SectionNo = 5
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None