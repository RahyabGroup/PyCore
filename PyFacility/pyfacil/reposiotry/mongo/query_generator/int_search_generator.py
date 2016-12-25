import datetime
import dateutil.parser
from pyutil.parser.type.type_parser import TypeParser

__author__ = 'H.Rouhani'


class IntSearchGenerator:
    field_name = None

    def __init__(self, field_name):
        self.field_name = field_name

    def generate(self, value):

        # in format:
        #  field_name<10
        # or field_name>10
        # or field_name=10
        # or field_name<10,field_name>10
        #  10<field_name<20 don't work
        # <= and >= don't work
        try:
            value = value.lstrip().rstrip()
            if '<' in value:
                values = value.split('<')
                if len(values) == 2:
                    if TypeParser.try_parse(values[1], int):
                        first_value = int(values[1])
                        return {self.field_name: {'$lt': first_value}}
            if '>' in value:
                values = value.split('>')
                if len(values) == 2:
                    if TypeParser.try_parse(values[1], int):
                        first_value = int(values[1])
                        return {self.field_name: {'$gt': first_value}}
            if '>=' in value:
                values = value.split('>=')
                if len(values) == 2:
                    if TypeParser.try_parse(values[1], int):
                        first_value = int(values[1])
                        return {self.field_name: {'$gte': first_value}}
            if '<=' in value:
                values = value.split('<=')
                if len(values) == 2:
                    if TypeParser.try_parse(values[1], int):
                        first_value = int(values[1])
                        return {self.field_name: {'$lte': first_value}}
            else:
                if TypeParser.try_parse(value, int):
                    first_value = int(value)
                    return {self.field_name: first_value}

        except Exception:
            return None

