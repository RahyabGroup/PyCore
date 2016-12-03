from bson import ObjectId
from pyfacil.web.query_string.query_string_criteria_emptiness_validation import QueryStringCriteriaEmptinessValidation
from pyfacil.web.query_string.query_string_fetch_validation import QueryStringFetchValidation
from pyfacil.web.query_string.query_string_ids_emptiness_validation import QueryStringIdsEmptinessValidation

__author__ = 'H.Rouhani'


class QueryStringInfo:
    skip = None
    take = None
    search_text = None
    sort = None
    operator = None
    criteria = None

    def __init__(self, default_operator="or", default_sort={'_id': -1}, default_take=150, default_skip=0):
        self.operator = default_operator
        self.sort = default_sort
        self.take = default_take
        self.skip = default_skip

    def load(self, query_string, check_criteria_emptiness=False):
        query_string_fetch_validation = QueryStringFetchValidation()
        query_string_fetch_validation.validate(query_string)

        if check_criteria_emptiness:
            query_string_criteria_emptiness_validation = QueryStringCriteriaEmptinessValidation()
            query_string_criteria_emptiness_validation.validate(query_string)

        if "skip" in query_string:
            self.skip = int(query_string["skip"])

        if "take" in query_string:
            self.take = int(query_string["take"])

        if "search_text" in query_string:
            self.search_text = query_string["search_text"]

        if "sort" in query_string:
            self.load_sort(query_string)

        if "operator" in query_string:
            self.operator = query_string["operator"]

        if "criteria" in query_string:
            self.load_criteria(query_string)

        if "ids" in query_string:
            self.load_ids(query_string)

    def load_sort(self, query_string):
        if query_string and query_string["sort"]:
            self.sort = {}
            sort_item = query_string["sort"]
            sort_list = sort_item.split(",")
            for sort_item in sort_list:
                sort_order_sign = sort_item[0:1]
                if sort_order_sign == "-":
                    sort_field_name = sort_item[1:]
                    self.sort[sort_field_name] = -1
                else:
                    self.sort[sort_item] = 1

    def load_criteria(self, query_string):
        if query_string and query_string["criteria"]:
            query_string_criteria_emptiness_validation = QueryStringCriteriaEmptinessValidation()
            query_string_criteria_emptiness_validation.validate(query_string)
            self.criteria = []
            criteria_item = query_string["criteria"]
            criteria_list = criteria_item.split(",")
            for criteria_item in criteria_list:
                criteria_item_list = criteria_item.split(":")
                criteria_field_name = criteria_item_list[0]
                criteria_field_value = criteria_item_list[1]
                self.criteria.append((criteria_field_name, criteria_field_value))

    def load_ids(self, query_string):
        if query_string and query_string["ids"]:
            query_string_ids_emptiness_validation = QueryStringIdsEmptinessValidation()
            query_string_ids_emptiness_validation.validate(query_string)
            self.ids = []
            ids_item = query_string['ids']
            ids_list = ids_item.split(",")
            [self.ids.append(ObjectId(id)) for id in ids_list]


