__author__ = 'h.rouhani'


class Custom:
    def __init__(self, validation):
        self._validation = validation

    def validate(self, item_to_validate, field_name=None):
        return self._validation.validate(item_to_validate, field_name)
