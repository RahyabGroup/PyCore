import unittest

from pyutil.serialization.json.serializer import Serializer
from test_pyutil.entity_helper.employee import Employee


__author__ = 'h.rouhani'


class TestSerializer(unittest.TestCase):
    def test_serializeToString_ShouldSerializeObjectToJsonStringFormat(self):
        employeeInstance = Employee.createSampleInstance()
        jsonSerializer = Serializer()
        employeeJsonString = jsonSerializer.serialize_to_string(employeeInstance)

        assert employeeJsonString is not None
        assert employeeJsonString.strip() != ""
        assert employeeJsonString.strip() != "null"
        assert isinstance(employeeJsonString, str)

    def test_serializeToDictionary_ShouldSerializeObjectToJsonDictionaryObject(self):
        employeeInstance = Employee.createSampleInstance()
        jsonSerializer = Serializer()
        employeeJsonDictionary = jsonSerializer.serialize_to_dictionary(employeeInstance)

        assert employeeJsonDictionary is not None
        assert isinstance(employeeJsonDictionary, dict)
        assert len(employeeJsonDictionary) > 0


