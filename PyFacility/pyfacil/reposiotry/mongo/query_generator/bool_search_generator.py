__author__ = 'H.Rouhani'


class BoolSearchGenerator:
    field_name = None

    def __init__(self, field_name):
        self.field_name = field_name

    def generate(self, value):
        try:
            value = value.lstrip().rstrip()
            if value.lower() in ['true', '1', 'yes']:
                return {self.field_name: True}
            if value.lower() in ['false', '0', 'no']:
                return {self.field_name: False}
        except Exception:
            return None

