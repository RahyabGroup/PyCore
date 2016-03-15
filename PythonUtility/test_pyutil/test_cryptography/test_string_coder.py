import unittest

from pyutil.cryptography.rsa.string_coder import StringCoder


__author__ = 'Hooman'


class TestStringCoder(unittest.TestCase):
    def setUp(self):
        self.key = "YyxuKKj7ir9NIfbM00C2DfBeTonX7t_uIAa-Vjbyqbg="
        self.rawString = "hello this is for cryptography test."

    def test_EncodeShouldEncryptGivenString(self):
        stringCoder = StringCoder(self.key)
        encodedString = stringCoder.encode(self.rawString)

        assert encodedString != None
        assert encodedString.strip() != ""

    def test_DecodeShouldDecryptGivenEncodedString(self):
        stringEncoder = StringCoder(self.key)
        encodedString = stringEncoder.encode(self.rawString)

        stringDecoder = StringCoder(self.key)
        decodedString = stringDecoder.decode(encodedString)

        assert decodedString == self.rawString
