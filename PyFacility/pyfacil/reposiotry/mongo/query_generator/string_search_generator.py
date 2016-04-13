__author__ = 'H.Rouhani'


class StringSearchGenerator:
    split_string = None
    string_splitter_operator = None
    field_name = None

    def __init__(self, field_name, split_string=True, string_splitter_operator="or"):
        self.field_name = field_name
        self.split_string = split_string
        self.string_splitter_operator = string_splitter_operator

    def generate(self, value):
        if not self.split_string:
            return {self.field_name: {'$regex': '.*{}.*'.format(value),
                                       '$options': '-i'}}
        else:
            text_criteria = {"${}".format(self.string_splitter_operator): []}
            for txt in value.split(" "):
                text_criteria["${}".format(self.string_splitter_operator)].append({self.field_name: {'$regex': '.*{}.*'.format(txt),
                                                                                                      '$options': '-i'}})
            return text_criteria
