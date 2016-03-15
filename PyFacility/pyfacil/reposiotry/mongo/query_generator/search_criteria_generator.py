__author__ = 'H.Rouhani'


class SearchCriteriaGenerator:
    template = None
    criteria = None
    operator = None

    def __init__(self, template, criteria, operator="or"):
        self.template = template
        self.criteria = criteria
        self.operator = operator

    def generate(self):
        if self.criteria:
            search_criteria = []
            for item in self.criteria:
                criteria_key = item[0]
                criteria_value = item[1]
                generator = self.template[criteria_key]
                generated_query = generator.generate(criteria_value)
                if generated_query:
                    search_criteria.append(generated_query)
            if search_criteria:
                return {'${}'.format(self.operator): search_criteria}
        return {}
