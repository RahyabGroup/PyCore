from datetime import datetime
import json

from test_pyutil.entity_helper.address import Address
from test_pyutil.entity_helper.office import Office


__author__ = 'h.rouhani'


class Employee:
    def _getName(self):
        return self.nameAttr

    def _setName(self, name):
        self.nameAttr = name

    def _getFamil(self):
        return self.familAttr

    def _setFamil(self, famil):
        self.familAttr = famil

    def _getOffice(self):
        return self.officeAttr

    def _setOffice(self, office):
        self.officeAttr = office

    def _getAddress(self):
        return self.addressAttr

    def _setAddress(self, address):
        self.addressAttr = address

    def _getBirthdate(self):
        return self._birthdate

    def _setBirthdate(self, birthdate):
        self._birthdate = birthdate

    Name = property(_getName, _setName)
    Famil = property(_getFamil, _setFamil)
    Office = property(_getOffice, _setOffice)
    Address = property(_getAddress, _setAddress)
    Birthdate = property(_getBirthdate, _setBirthdate)

    @staticmethod
    def createSampleInstance():
        employeeInstance = Employee()
        employeeInstance.Birthdate = datetime.now()
        employeeInstance.Name = "Hooman"
        employeeInstance.Famil = "Rouhani"
        employeeInstance.Office = Office()
        employeeInstance.Office.Name = "Developer"
        employeeInstance.Office.Code = 13
        employeeInstance.Address = []
        address1 = Address()
        address1.Street = "Pasdaran"
        address1.Avenue = "Golestane dovom"
        address2 = Address()
        address2.Street = "Farmanieh"
        address2.Avenue = "Simin Dokht"
        employeeInstance.Address.append(address1)
        employeeInstance.Address.append(address2)

        return employeeInstance

    @staticmethod
    def createSampleJson():
        return '''{
                   "familAttr":"Rouhani",
                   "_birthdate":"2015-08-01T13:00:12.120976",
                   "nameAttr":"Hooman",
                   "officeAttr":{
                      "py/object":"test_pyutil.entity_helper.office.Office",
                      "codeAttr":13,
                      "nameAttr":"Developer"
                   },
                   "py/object":"test_pyutil.entity_helper.employee.Employee",
                   "addressAttr":[
                      {
                         "py/object":"test_pyutil.entity_helper.address.Address",
                         "streetAttr":"Pasdaran",
                         "avenueAttr":"Golestane dovom"
                      },
                      {
                         "py/object":"test_pyutil.entity_helper.address.Address",
                         "streetAttr":"Farmanieh",
                         "avenueAttr":"Simin Dokht"
                      }
                   ]
                }'''

    @staticmethod
    def createSampleDictionary():
        employeeJsonString = Employee.createSampleJson()
        dataJsonDictionary = json.loads(employeeJsonString)
        return dataJsonDictionary