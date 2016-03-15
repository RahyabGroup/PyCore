from pyfacil.model.aggregate_root import AggregateRoot


__author__ = 'H.Rouhani'


class SearchableAggregateRoot(AggregateRoot):
    @classmethod
    def simple_search_async(cls, search_text, skip, take, sort={"_id": -1}):
        return (yield from cls.reader.simple_search(search_text, skip, take, sort))

    @classmethod
    def simple_search(cls, search_text, skip, take, sort={"_id": -1}):
        return cls.reader.simple_search(search_text, skip, take, sort)

    @classmethod
    def advanced_search_async(cls, criteria, skip, take, operator, sort={"_id": -1}):
        return (yield from cls.reader.advanced_search(criteria, skip, take, operator, sort))

    @classmethod
    def advanced_search(cls, criteria, skip, take, operator, sort={"_id": -1}):
        return cls.reader.advanced_search(criteria, skip, take, operator, sort)