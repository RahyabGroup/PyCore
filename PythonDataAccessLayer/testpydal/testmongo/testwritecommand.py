import unittest

from bson import ObjectId

from testpydal.entityhelper.employee import Employee
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestWriteCommand(unittest.TestCase):
    def test_save_ShouldCreateNewDocument(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.save(employee)

        assert hasattr(employee, "_id")
        assert employee._id is not None
        assert employee._id != ""
        assert type(employee._id) == str

    def test_save_ShouldUpdateCreatedDocument(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        assert not hasattr(employee, "_id")
        pydalCollectionInstance.writer.save(employee)
        assert hasattr(employee, "_id")
        createdEmployeeId = employee._id
        employee.Name = employee.Name + " - Edited"
        pydalCollectionInstance.writer.save(employee)
        editedEmployeeId = employee._id
        assert createdEmployeeId == editedEmployeeId

    def test_add_ShouldCreateDocumentInMondoDb(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        pydalCollectionInstance.writer.add(employee)
        assert hasattr(employee, "_id")
        assert employee._id is not None
        assert employee._id != ""
        assert type(employee._id) == str

    def test_edit_ShouldUpdateAvailableDocumentInMongoDb(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        assert not hasattr(employee, "_id")
        pydalCollectionInstance.writer.add(employee)
        assert hasattr(employee, "_id")
        createdEmployeeId = employee._id
        employee.Name = employee.Name + " - Edited"
        pydalCollectionInstance.writer.edit(employee)
        editedEmployeeId = employee._id
        assert createdEmployeeId == editedEmployeeId

    def test_editByCondition_ShouldExecuteSecondQueryOnElementsOfDocumentsWhichAreUnderFirstQueryCondition(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        mongoDeveloperCollection = pydalCollectionInstance._mongo_collection
        pydalCollectionInstance.writer.add(employee)
        addedEmployee = mongoDeveloperCollection.find_one({"_id": ObjectId(employee._id)})
        assert len(addedEmployee["address"]) == 2
        pydalCollectionInstance.writer.edit_by_condition({"_id": ObjectId(employee._id)}, {"$pull": {"address": {"street": "Farmanieh"}}})
        editedEmployee = mongoDeveloperCollection.find_one({"_id": ObjectId(employee._id)})
        assert len(editedEmployee["address"]) == 1

    def test_removeById_ShouldRemoveDocumentInMongoDbByItsId(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        mongoDeveloperCollection = pydalCollectionInstance._mongo_collection
        pydalCollectionInstance.writer.add(employee)
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() > 0
        pydalCollectionInstance.writer.remove_by_id(employee._id)
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() == 0

    def test_removeByCondition_ShouldRemoveDocumentsInMongoDbIfTheConditionIsEstablishedForThem(self):
        employee = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        mongoDeveloperCollection = pydalCollectionInstance._mongo_collection
        pydalCollectionInstance.writer.add(employee)
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() > 0
        pydalCollectionInstance.writer.remove_by_condition({"_id": ObjectId(employee._id)})
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() == 0

    def test_removeAll_ShouldRemoveAllDocumentsInCollection(self):
        employee = Employee.createSampleInstance()
        employee1 = Employee.createSampleInstance()
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        mongoDeveloperCollection = pydalCollectionInstance._mongo_collection
        pydalCollectionInstance.writer.add(employee)
        pydalCollectionInstance.writer.add(employee1)
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() > 0
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee1._id)}).count() > 0
        pydalCollectionInstance.writer.remove_all()
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee._id)}).count() == 0
        assert mongoDeveloperCollection.find({"_id": ObjectId(employee1._id)}).count() == 0
