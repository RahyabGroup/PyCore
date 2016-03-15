import unittest

from bson import ObjectId
from pymongo.cursor import Cursor

from testpydal.entityhelper.employee import Employee
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestCappedReadCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.capped_collection = InstanceFactory.createPydalCappedCollectionInstance()

    def test_count_ShouldGetCountOfDocumentBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        employee1 = Employee.createSampleInstance()
        TestCappedReadCommand.capped_collection.writer.add(employee)
        TestCappedReadCommand.capped_collection.writer.add(employee1)
        assert TestCappedReadCommand.capped_collection.reader.count({"name": employee.Name}) > 0
        assert TestCappedReadCommand.capped_collection.reader.count({"name": employee1.Name}) > 0

    def test_findOne_ShouldFindOneDocumentBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        TestCappedReadCommand.capped_collection.writer.add(employee)
        foundedEmployee = TestCappedReadCommand.capped_collection.reader.find_one({"_id": ObjectId(employee._id)})
        assert foundedEmployee.Name == employee.Name
        assert foundedEmployee._id == employee._id

    def test_findMany_ShouldFindManyDocumentsBasedOnQuery(self):
        employee = Employee.createSampleInstance()
        TestCappedReadCommand.capped_collection.writer.add(employee)
        employee._id = str(ObjectId())
        TestCappedReadCommand.capped_collection.writer.add(employee)
        foundedEmployees = TestCappedReadCommand.capped_collection.reader.find_many({"name": employee.Name})
        assert len(foundedEmployees) > 0
        assert foundedEmployees[0].Name == employee.Name

    def test_isAvailable_ShouldCheckIfDocumentIsAvailable(self):
        employee = Employee.createSampleInstance()
        TestCappedReadCommand.capped_collection.writer.add(employee)
        assert TestCappedReadCommand.capped_collection.reader.is_available({"name": employee.Name}) == True
        assert TestCappedReadCommand.capped_collection.reader.is_available({"_id": ObjectId(employee._id)}) == True
        assert TestCappedReadCommand.capped_collection.reader.is_available({"_id": ObjectId()}) == False

    def test_open_tailable_cursor_should_return_tailable_cursor_for_given_query(self):
        employee = Employee.createSampleInstance()
        TestCappedReadCommand.capped_collection.writer.add(employee)
        employee._id = str(ObjectId())
        TestCappedReadCommand.capped_collection.writer.add(employee)
        cursor = TestCappedReadCommand.capped_collection.reader.open_tailable_cursor({"name": employee.Name})
        assert isinstance(cursor, Cursor)
        assert cursor.count() > 0
        for item in cursor:
            assert item["name"] == employee.Name
