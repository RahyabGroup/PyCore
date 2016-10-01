from pyutil.parser.type.type_parser import TypeParser

__author__ = 'H.Rouhani'


class ListSearchGenerator:
    field_name = None
    list_items_type = None

    def __init__(self, field_name, list_items_type=int):
        self.field_name = field_name
        self.list_items_type = list_items_type

    def generate(self, value):
        if TypeParser.try_parse(value, list):
            return {self.field_name: {"$in": value}}
        elif TypeParser.try_parse(value, self.list_items_type):
                return {self.field_name: {"$in": list([self.list_items_type(value)])}}
        return None
