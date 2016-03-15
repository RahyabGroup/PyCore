from pyvalidate.validation import Validation

__author__ = 'H.Rouhani'


class QueryStringFetchValidation(Validation):
    def validate(self, query_string):
        if "take" in query_string:
            take = int(query_string["take"])
            super().integer.size(take, 0, 150)
        super().validate()
