import unittest

from pyutil.cryptography.rsa.object_coder import ObjectCoder
from test_pyutil.entity_helper.employee import Employee

__author__ = 'Hooman'


class TestObjectCoder(unittest.TestCase):
    def setUp(self):
        self.key = "YyxuKKj7ir9NIfbM00C2DfBeTonX7t_uIAa-Vjbyqbg="
        self.object = Employee.createSampleInstance()

    def test_EncodeShouldEncryptGivenString(self):
        objectCoder = ObjectCoder(self.key)
        encodedString = objectCoder.encode(self.object)

        assert encodedString != None
        assert encodedString.strip() != ""

    def test_DecodeShouldDecryptGivenEncodedString(self):
        objectEncoder = ObjectCoder(self.key)
        encodedString = objectEncoder.encode(self.object)

        objectDecoder = ObjectCoder(self.key)
        decodedObject = objectDecoder.decode(encodedString)

        assert type(decodedObject) == Employee