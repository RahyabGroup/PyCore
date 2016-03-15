import pymongo

__author__ = 'H.Rouhani'


class GridfsRead:
    def __init__(self, fs):
        self._fs = fs

    def get(self, id):
        file = self._fs.get(id)
        result = self._get_result(file)
        return result

    def find_one(self, query):
        file = self._fs.find_one(query)
        result = self._get_result(file)
        return result

    def find_many(self, query, skip=0, take=10, sort={'_id': pymongo.DESCENDING}):
        sort = [(k, v) for k, v in sort.items()]
        files = self._fs.find(query).skip(skip).limit(take).sort(sort)
        result = []
        for file in files:
            result.append(self._get_result(file))
        return result

    def is_available_id(self, id):
        return self._fs.exists(id)

    def is_available(self, query):
        return self._fs.exists(query)

    def _get_result(self, file):
        result = {"binary_data": file.read(),
                  "info": file._file}
        return result
