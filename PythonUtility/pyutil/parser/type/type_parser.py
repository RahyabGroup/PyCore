__author__ = 'H.Rouhani'


class TypeParser:
    @staticmethod
    def try_parse(value, type_to_try):
        try:
            result = type_to_try(value)
            return result
        except:
            return None
