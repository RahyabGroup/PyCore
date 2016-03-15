from pyutil.parser.type.type_parser import TypeParser

__author__ = 'H.Rouhani'


class TypeSearchGenerator:
    field_name = None
    field_type = None

    def __init__(self, field_name, field_type):
        self.field_name = field_name
        self.field_type = field_type

    def generate(self, value):
        if TypeParser.try_parse(value, self.field_type):
            return {self.field_name: self.field_type(value)}
        return None