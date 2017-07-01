from pyvalidate.validation import Validation

__author__ = 'R.Azh'


class EnglishEmployeeValidation(Validation):
    def validate(self, employee):
        super().string.size(employee.Name, 3, 15, True)
        super().string.only_english(employee.Name, False)
        return super().validate()
