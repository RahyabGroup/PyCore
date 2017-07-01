from pyvalidate.validation import Validation

__author__ = 'R.Azh'


class PersianEmployeeValidation(Validation):
    def validate(self, employee):
        super().string.size(employee.Name, 3, 15, True)
        super().string.only_persian(employee.Name, False)
        return super().validate()
