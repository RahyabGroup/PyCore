import unittest
from pyvalidate.exception.validation_exception import ValidationException
from testpyvalidate.entity_helper.office import Office
from testpyvalidate.validation_helper.office_validation import OfficeValidation

__author__ = 'H.Rouhani'


class TestDatetime(unittest.TestCase):
    def test_available_date_string_validation_should_accept_string_of_date_time(self):
        valid_date_string = '2015-07-05 09:42:29.502653'
        office = Office()
        office.date = valid_date_string
        office.Code = -1
        office.UnitNumber = 0
        office.FloorNo = 10
        office.SectionNo = 5
        officeValidation = OfficeValidation()
        result = officeValidation.validate(office)
        assert result is None

    def test_available_date_string_validation_should_not_accept_string_of_none_date_time(self):
        try:
            valid_date_string = 'not date time string!!'
            office = Office()
            office.date = valid_date_string
            office.Code = -1
            office.UnitNumber = 0
            office.FloorNo = 10
            office.SectionNo = 5
            officeValidation = OfficeValidation()
            result = officeValidation.validate(office)
            assert result is not None
        except ValidationException as ex:
            assert ex.Errors
