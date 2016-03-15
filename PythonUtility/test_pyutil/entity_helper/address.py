__author__ = 'h.rouhani'


class Address:
    def _getStreet(self):
        return self.streetAttr

    def _setStreet(self, street):
        self.streetAttr = street

    def _getAvenue(self):
        return self.avenueAttr

    def _setAvenue(self, avenue):
        self.avenueAttr = avenue

    Street = property(_getStreet, _setStreet)
    Avenue = property(_getAvenue, _setAvenue)
