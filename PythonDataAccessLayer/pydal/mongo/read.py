import pymongo
from pyutil.serialization.json.deserializer import Deserializer

__author__ = 'Hooman'


class ReadCommand:
    def __init__(self, mongo_collection):
        self._mongo_collection = mongo_collection

    def count(self, query=None):
        if query is None:
            document_count = self._mongo_collection.find().count()
        else:
            document_count = self._mongo_collection.find(query).count()
        return document_count

    def find_one(self, query, fields=[]):
        projection = None
        if fields:
            fields.append("py/object")
            projection = dict.fromkeys(fields, 1)
        document = self._mongo_collection.find_one(query, projection)
        if document is None:
            return None
        return self._get_result(document)

    def find_many(self, query, fields=[], skip=0, take=50, sort={'_id': pymongo.DESCENDING}):
        sort = [(k, v) for k, v in sort.items()]
        projection = None
        if fields:
            fields.append("py/object")
            projection = dict.fromkeys(fields, 1)
        documents = self._mongo_collection.find(query, projection, skip=skip, limit=take, sort=sort)
        return self._get_results(documents)

    def is_available(self, query):
        return self._mongo_collection.find_one(query, {"_id": 1}) is not None

    def aggregate(self, fields=[], skip=0, take=50, sort={'_id': pymongo.DESCENDING}, query=[], cursor={}):
        aggregate_query = []
        aggregate_query.extend(query)
        if fields:
            fields.append("py/object")
            aggregate_query.append({"$project": dict.fromkeys(fields, 1)})
        aggregate_query.append({"$sort": sort})
        if skip:
            aggregate_query.append({"$skip": skip})
        if take:
            aggregate_query.append({"$limit": take})
        documents = self._mongo_collection.aggregate(aggregate_query)
        return self._get_results(documents)

    def aggregate_count(self, query=[], fields=[], cursor={}):
        aggregate_query = []
        aggregate_query.extend(query)
        if fields:
            fields.append("py/object")
            aggregate_query.append({"$project": dict.fromkeys(fields, 1)})
        else:
            aggregate_query.append({"$project": {"_id": 1}})
        documents = self._mongo_collection.aggregate(aggregate_query)
        return len(self._get_results(documents))

    def _get_results(self, documents):
        results = []
        if documents:
            for document in documents:
                results.append(self._get_result(document))
        return results

    def _get_result(self, document):
        result = None
        if document:
            json_deserializer = Deserializer()
            json_deserializer.add_backend("bson.json_util")
            result = json_deserializer.deserialize_from_dictionary(document)
            if isinstance(result, dict):
                result["_id"] = str(result["_id"])
            else:
                result._id = str(result._id)
        return result
