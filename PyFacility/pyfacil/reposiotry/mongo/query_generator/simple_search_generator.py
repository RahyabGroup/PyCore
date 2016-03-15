__author__ = 'H.Rouhani'


class SimpleSearchGenerator:
    __generators = None
    search_text = None
    operator = None

    def __init__(self, search_text, operator="or"):
        self.search_text = search_text
        self.operator = operator
        self.__generators = []

    def register_generator(self, generator):
        self.__generators.append(generator)

    def generate(self):
        if self.search_text and self.search_text.strip() and self.__generators:
            search_criteria = []
            for generator in self.__generators:
                generated_query = generator.generate(self.search_text)
                if generated_query:
                    search_criteria.append(generated_query)
            if search_criteria:
                return {'${}'.format(self.operator): search_criteria}
        return {}
