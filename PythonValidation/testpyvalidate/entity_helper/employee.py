from bson import ObjectId
from testpyvalidate.entity_helper.address import Address
from testpyvalidate.entity_helper.office import Office


__author__ = 'h.rouhani'


class Employee:
    def __init__(self):
        # self._setId(str(ObjectId()))
        self._id = str(ObjectId())
        self.phones = []
        self.addresses = []
        self.office = Office()

    def _getName(self):
        return self.name

    def _setName(self, name):
        self.name = name

    def _getOffice(self):
        return self.office

    def _setOffice(self, office):
        self.office = office

    def _getAddresses(self):
        return self.addresses

    def _setAddresses(self, addresses):
        self.addresses = addresses

    def _getPhones(self):
        return self.phones

    def _setPhones(self, phones):
        self.phones = phones

    # fixme
    # def _getId(self):
    #     return self._id
    #
    # def _setId(self, val):
    #     self._id = val

    Name = property(_getName, _setName)
    Office = property(_getOffice, _setOffice)
    Addresses = property(_getAddresses, _setAddresses)
    Phones = property(_getPhones, _setPhones)
    # _id = property(_getId, _setId)

