import unittest
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestDb(unittest.TestCase):
    def test_collection_ShouldCreatePydalCollectionWithMongoDbCollectionInside(self):
        pydalCollection = InstanceFactory.createPydalCollectionInstance()

        assert pydalCollection is not None
        assert pydalCollection.collection_name == InstanceFactory.mongoCollectionName()

        assert pydalCollection._mongo_collection is not None
        assert pydalCollection._mongo_collection.name == InstanceFactory.mongoCollectionName()
        assert pydalCollection._mongo_collection.full_name == InstanceFactory.mongoDbName() + "." + InstanceFactory.mongoCollectionName()
