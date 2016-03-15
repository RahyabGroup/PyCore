import unittest

from bson import ObjectId

from testpydal.entityhelper.employee import Employee
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestReadCommand(unittest.TestCase):
    def test_count_ShouldGetCountOfDocumentBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        employee1 = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.add(employee)
        pydalCollectionInstance.writer.add(employee1)
        assert pydalCollectionInstance.reader.count({"name": employee.Name}) > 0
        assert pydalCollectionInstance.reader.count({"name": employee1.Name}) > 0

    def test_findOne_ShouldFindOneDocumentBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.add(employee)
        foundedEmployee = pydalCollectionInstance.reader.find_one({"_id": ObjectId(employee._id)})
        assert foundedEmployee.Name == employee.Name
        assert foundedEmployee._id == employee._id

    def test_findMany_ShouldFindManyDocumentsBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.add(employee)
        employee._id = str(ObjectId())
        pydalCollectionInstance.writer.add(employee)
        foundedEmployees = pydalCollectionInstance.reader.find_many({"name": employee.Name})
        assert len(foundedEmployees) > 0
        assert foundedEmployees[0].Name == employee.Name

    def test_isAvailable_ShouldCheckIfDocumentIsAvailable(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.add(employee)
        assert pydalCollectionInstance.reader.is_available({"name": employee.Name}) == True
        assert pydalCollectionInstance.reader.is_available({"_id": ObjectId(employee._id)}) == True
        assert pydalCollectionInstance.reader.is_available({"_id": ObjectId()}) == False
