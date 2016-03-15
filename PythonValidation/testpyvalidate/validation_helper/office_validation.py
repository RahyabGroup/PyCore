from pyvalidate.validation import Validation

__author__ = 'Hooman'


class OfficeValidation(Validation):
    def validate(self, office):
        super().integer.negative(office.Code, False)
        super().integer.negative(office.UnitNumber, True)
        super().integer.positive(office.FloorNo, False)
        super().integer.positive(office.SectionNo, True)
        super().integer.size(office.FloorNo, 2, 15)
        super().date.available_date_string(office.Date, False)
        if office.sectionNo == 753:
            super().custom.manual({"body": "SECTION_NUMBER_NOT_AVAILABLE", "code": "err403"})
        return super().validate()
