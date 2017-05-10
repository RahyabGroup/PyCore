from pyvalidate.create_result_message import create_result_message

__author__ = 'Hooman'


class Manual:
    data = None
    field_name = None

    def __init__(self, data=""):
        self.data = data

    def validate(self, validation_error_code, field_name=None):
        return create_result_message(validation_error_code, field_name, self.data)
