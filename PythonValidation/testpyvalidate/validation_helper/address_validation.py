from pyvalidate.validation import Validation

__author__ = 'Hooman'


class AddressValidation(Validation):
    def validate(self, address):
        super().string.email(address.Email)
        super().string.text_size(address.Street, 2, 5)
        super().string.only_string(address.Street)
        return super().validate()