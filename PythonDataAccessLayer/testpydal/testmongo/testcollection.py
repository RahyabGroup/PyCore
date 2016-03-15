import unittest
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestCollection(unittest.TestCase):
    def test_Reader_ShouldReturnPydalReadCommandWithMongoCollectionInside(self):
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        self._checkCorrectionOfPydalCollectionReaderOrWriterInitialization(pydalCollectionInstance.reader, pydalCollectionInstance)


    def test_Writer_ShouldReturnPydalWriteCommandWithMongoCollectionInside(self):
        pydalCollectionInstance = InstanceFactory.createPydalCollectionInstance()
        self._checkCorrectionOfPydalCollectionReaderOrWriterInitialization(pydalCollectionInstance.writer, pydalCollectionInstance)

    def _checkCorrectionOfPydalCollectionReaderOrWriterInitialization(self, pydalReaderOrWriterInstance,
                                                                      pydalCollectionInstance):
        assert pydalReaderOrWriterInstance is not None
        assert pydalReaderOrWriterInstance._mongo_collection is not None
        assert pydalReaderOrWriterInstance._mongo_collection == pydalCollectionInstance._mongo_collection


