from bson import ObjectId
from pydal.mongo.connection import Connection

__author__ = 'Hooman'


class InstanceFactory:
    @staticmethod
    def createPydalConnectionInstance():
        pydalConnection = Connection(InstanceFactory.mongoConnection())
        return pydalConnection

    @staticmethod
    def createPydalDbInstance():
        pydalConnection = Connection(InstanceFactory.mongoConnection())
        pydalDb = pydalConnection.db(InstanceFactory.mongoDbName())
        return pydalDb

    @staticmethod
    def createPydalCollectionInstance():
        pydalConnection = Connection(InstanceFactory.mongoConnection())
        pydalCollection = pydalConnection \
            .db(InstanceFactory.mongoDbName()) \
            .collection(InstanceFactory.mongoCollectionName())
        return pydalCollection

    @staticmethod
    def createPydalCappedCollectionInstance():
        pydalConnection = Connection(InstanceFactory.mongoConnection())
        pydalCollection = pydalConnection \
            .db(InstanceFactory.mongoDbName()) \
            .capped_collection(InstanceFactory.mongoCappedCollectionName())
        return pydalCollection

    @staticmethod
    def mongoConnection():
        return "mongodb://localhost:27017"

    @staticmethod
    def mongoDbName():
        return "pydalDb"

    @staticmethod
    def mongoCollectionName():
        return "Developer"

    @staticmethod
    def mongoCappedCollectionName():
        return "capped_developer"


