from datetime import datetime
import unittest

from pyutil.serialization.json.deserializer import Deserializer
from test_pyutil.entity_helper.employee import Employee


__author__ = 'h.rouhani'


class TestDeserializer(unittest.TestCase):
    def test_deserializeFromString_ShouldDesrializeJsonStringFormatToRelatedObject(self):
        employeeJsonString = Employee.createSampleJson()
        jsonDeserializer = Deserializer()
        employeeInstance = jsonDeserializer.deserialize_from_string(employeeJsonString)

        datetime.now().isoformat()

        assert employeeInstance is not None
        assert employeeInstance.Birthdate is not None
        assert isinstance(employeeInstance, Employee)

    def test_deserializeFromDictionary_ShouldDeserializeJsonDictionaryObjecToRelatedObject(self):
        employeeJsonDictionary = Employee.createSampleDictionary()
        jsonDeserializer = Deserializer()
        employeeInstance = jsonDeserializer.deserialize_from_dictionary(employeeJsonDictionary)

        assert employeeInstance is not None
        assert employeeInstance.Birthdate is not None
        assert isinstance(employeeInstance, Employee)