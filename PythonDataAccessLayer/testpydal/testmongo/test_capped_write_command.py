import unittest

from bson import ObjectId

from testpydal.entityhelper.employee import Employee
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestCappedWriteCommand(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.capped_collection = InstanceFactory.createPydalCappedCollectionInstance()

    def test_save_ShouldCreateNewDocument(self):
        employee = Employee.createSampleInstance()
        TestCappedWriteCommand.capped_collection.writer.save(employee)

        assert hasattr(employee, "_id")
        assert employee._id is not None
        assert employee._id != ""
        assert type(employee._id) == str

    def test_save_ShouldUpdateCreatedDocument(self):
        employee = Employee.createSampleInstance()
        employee.Name = 1
        assert not hasattr(employee, "_id")
        TestCappedWriteCommand.capped_collection.writer.save(employee)
        assert hasattr(employee, "_id")
        createdEmployeeId = employee._id
        employee.Name = 0
        TestCappedWriteCommand.capped_collection.writer.edit(employee)
        editedEmployeeId = employee._id
        assert createdEmployeeId == editedEmployeeId

    def test_add_ShouldCreateDocumentInMondoDb(self):
        employee = Employee.createSampleInstance()
        TestCappedWriteCommand.capped_collection.writer.add(employee)
        assert hasattr(employee, "_id")
        assert employee._id is not None
        assert employee._id != ""
        assert type(employee._id) == str

    def test_edit_ShouldUpdateAvailableDocumentInMongoDb(self):
        employee = Employee.createSampleInstance()
        employee.Name = 0
        assert not hasattr(employee, "_id")
        TestCappedWriteCommand.capped_collection.writer.add(employee)
        assert hasattr(employee, "_id")
        createdEmployeeId = employee._id
        employee.Name = 1
        TestCappedWriteCommand.capped_collection.writer.edit(employee)
        editedEmployeeId = employee._id
        assert createdEmployeeId == editedEmployeeId

    def test_editByCondition_ShouldExecuteSecondQueryOnElementsOfDocumentsWhichAreUnderFirstQueryCondition(self):
        employee = Employee.createSampleInstance()
        mongoDeveloperCollection = TestCappedWriteCommand.capped_collection._mongo_collection
        TestCappedWriteCommand.capped_collection.writer.add(employee)
        addedEmployee = mongoDeveloperCollection.find_one({"_id": ObjectId(employee._id)})
        assert len(addedEmployee["address"]) == 2
        TestCappedWriteCommand.capped_collection.writer.edit_by_condition({"_id": ObjectId(employee._id)}, {"$pull": {"address": {"street": "Farmanieh"}}})
        editedEmployee = mongoDeveloperCollection.find_one({"_id": ObjectId(employee._id)})
        assert len(editedEmployee["address"]) == 1
