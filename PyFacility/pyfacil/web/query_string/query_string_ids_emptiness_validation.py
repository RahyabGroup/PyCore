from pyvalidate.validation import Validation
from pyfacil.web.rest.resource import ErrorCodes

__author__ = 'root'


class QueryStringIdsEmptinessValidation(Validation):
    def validate(self, query_string):
        if "ids" in query_string:
            ids = query_string["ids"]
            if not ids.strip():
                super().custom.manual(ErrorCodes.SEARCH_ID_LIST_IS_EMPTY)
        else:
            super().custom.manual(ErrorCodes.SEARCH_ID_LIST_IS_EMPTY)
        super().validate()
