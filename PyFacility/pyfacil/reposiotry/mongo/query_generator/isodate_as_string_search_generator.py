import datetime
import dateutil.parser

__author__ = 'H.Rouhani'


class IsoDateAsStringSearchGenerator:
    split_string = None
    string_splitter_operator = None
    field_name = None

    def __init__(self, field_name):
        self.field_name = field_name

    def generate(self, value):
        try:
            if '~' not in value:
                date = dateutil.parser.parse(value) + datetime.timedelta(hours=23, minutes=59, seconds=59)
                return {'$and': [{self.field_name: {'$gt': value}}, {self.field_name: {'$lt': date.isoformat()}}]}
            else:
                value = value.lstrip('(').rstrip(')')
                dates = value.split('~')
                if dateutil.parser.parse(dates[0]) <= dateutil.parser.parse(dates[1]):
                    first_date = dateutil.parser.parse(dates[0])
                    second_date = dateutil.parser.parse(dates[1]) + datetime.timedelta(hours=23, minutes=59, seconds=59)
                else:
                    first_date = dateutil.parser.parse(dates[1])
                    second_date =dateutil.parser.parse(dates[0]) + datetime.timedelta(hours=23, minutes=59, seconds=59)
                return {'$and': [{self.field_name: {'$gt': first_date.isoformat()}},
                                 {self.field_name: {'$lt': second_date.isoformat()}}]}
        except Exception:
            return None

