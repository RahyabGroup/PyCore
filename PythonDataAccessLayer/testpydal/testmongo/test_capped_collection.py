import unittest
from testpydal.testmongo.instancefactory import InstanceFactory

__author__ = 'Hooman'


class TestCappedCollection(unittest.TestCase):
    def test_Capped_Reader_ShouldReturnPydalCappedReadCommandWithMongoCollectionInside(self):
        pydalCappedCollectionInstance = InstanceFactory.createPydalCappedCollectionInstance()
        self._checkCorrectionOfPydalCollectionReaderOrWriterInitialization(pydalCappedCollectionInstance.reader, pydalCappedCollectionInstance)


    def test_Capped_Writer_ShouldReturnPydalCappedWriteCommandWithMongoCollectionInside(self):
        pydalCappedCollectionInstance = InstanceFactory.createPydalCappedCollectionInstance()
        self._checkCorrectionOfPydalCollectionReaderOrWriterInitialization(pydalCappedCollectionInstance.writer, pydalCappedCollectionInstance)

    def _checkCorrectionOfPydalCollectionReaderOrWriterInitialization(self, pydalReaderOrWriterInstance,
                                                                      pydalCollectionInstance):
        assert pydalReaderOrWriterInstance is not None
        assert pydalReaderOrWriterInstance._mongo_collection is not None
        assert pydalReaderOrWriterInstance._mongo_collection == pydalCollectionInstance._mongo_collection


