__author__ = 'h.rouhani'


class Address:
    def _getStreet(self):
        return self.street

    def _setStreet(self, street):
        self.street = street

    def _getAvenue(self):
        return self.avenue

    def _setAvenue(self, avenue):
        self.avenue = avenue

    Street = property(_getStreet, _setStreet)
    Avenue = property(_getAvenue, _setAvenue)
