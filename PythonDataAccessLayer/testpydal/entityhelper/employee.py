import json
from pyutil.serialization.json.serializer import Serializer

from testpydal.entityhelper.address import Address
from testpydal.entityhelper.office import Office

__author__ = 'h.rouhani'


class Employee:
    def _getName(self):
        return self.name

    def _setName(self, name):
        self.name = name

    def _getFamil(self):
        return self.famil

    def _setFamil(self, famil):
        self.famil = famil

    def _getOffice(self):
        return self.office

    def _setOffice(self, office):
        self.office = office

    def _getAddress(self):
        return self.address

    def _setAddress(self, address):
        self.address = address

    Name = property(_getName, _setName)
    Famil = property(_getFamil, _setFamil)
    Office = property(_getOffice, _setOffice)
    Address = property(_getAddress, _setAddress)

    @staticmethod
    def createSampleInstance():
        employeeInstance = Employee()
        employeeInstance.Name = "masood"
        employeeInstance.Famil = "khaari"
        employeeInstance.Office = Office()
        employeeInstance.Office.Name = "Developer"
        employeeInstance.Office.Code = 13
        employeeInstance.Address = []
        address1 = Address()
        address1.Street = "arjantin"
        address1.Avenue = "Golestane dovom"
        address2 = Address()
        address2.Street = "Farmanieh"
        address2.Avenue = "Simin Dokht"
        employeeInstance.Address.append(address1)
        employeeInstance.Address.append(address2)

        return employeeInstance

    @staticmethod
    def createSampleJson():
        json_serializer = Serializer()
        return json_serializer.serialize_to_string(Employee.createSampleInstance())

    @staticmethod
    def createSampleDictionary():
        employeeJsonString = Employee.createSampleJson()
        dataJsonDictionary = json.loads(employeeJsonString)
        return dataJsonDictionary