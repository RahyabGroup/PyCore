from pyvalidate.validation import Validation
from pyfacil.web.rest.resource import ErrorCodes

__author__ = 'H.Rouhani'


class QueryStringCriteriaEmptinessValidation(Validation):
    def validate(self, query_string):
        if "criteria" in query_string:
            criteria = query_string["criteria"]
            if not criteria.strip():
                super().custom.manual(ErrorCodes.SEARCH_CRITERIA_IS_NOT_DEFINED)
        else:
            super().custom.manual(ErrorCodes.SEARCH_CRITERIA_IS_NOT_DEFINED)
        super().validate()
