import unittest
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestConnection(unittest.TestCase):
    def test_init_ShouldInitializePydalConnectionWithMongoConnectionInside(self):
        pydalConnection = InstanceFactory.createPydalConnectionInstance()

        assert pydalConnection is not None
        assert pydalConnection._connection_string == InstanceFactory.mongoConnection()

        assert pydalConnection._mongo_connection is not None

    def test_db_ShouldCreatePydalDbWithMongoDbDatabaseInside(self):
        pydalDb = InstanceFactory.createPydalDbInstance()

        assert pydalDb is not None
        assert pydalDb.db_name == InstanceFactory.mongoDbName()

        assert pydalDb.mongodb is not None
        assert pydalDb.mongodb.name == InstanceFactory.mongoDbName()


