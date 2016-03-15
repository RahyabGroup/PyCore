__author__ = 'H.Rouhani'


class GridfsWrite:
    def __init__(self, fs):
        self._fs = fs

    def add(self, binary_data, **kwargs):
        file_id = self._fs.put(binary_data, **kwargs)
        return str(file_id)

    def remove(self, id):
        self._fs.delete(id)

    def remove_by_condition(self, query):
        results = self._fs.find(query)
        for result in results:
            self.remove(result._id)