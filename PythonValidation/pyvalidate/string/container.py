from pyvalidate.string.available_date_string import AvailableDateString
from pyvalidate.string.email import Email
from pyvalidate.string.empty import Empty
from pyvalidate.string.equality import Equality
from pyvalidate.string.object_id import ObjectId
from pyvalidate.string.only_english import OnlyEnglish
from pyvalidate.string.only_persian import OnlyPersian
from pyvalidate.string.only_string import OnlyString
from pyvalidate.string.size import Size
from pyvalidate.string.text_size import TextSize
from pyvalidate.validation_container import ValidationContainer

__author__ = 'h.rouhani'


class Container(ValidationContainer):
    def size(self, string, min_size=None, max_size=None, none_exception=True):
        string_size_validation = Size(min_size, max_size)
        return self._execute(string, string_size_validation, none_exception)

    def text_size(self, string, min_size=None, max_size=None, none_exception=True):
        text_size_validation = TextSize(min_size, max_size)
        return self._execute(string, text_size_validation, none_exception)

    def email(self, email, none_exception=True):
        email_validation = Email()
        return self._execute(email, email_validation, none_exception)

    def only_string(self, string, none_exception=True):
        only_string_validation = OnlyString()
        return self._execute(string, only_string_validation, none_exception)

    def equality(self, string, compare_with, none_exception=True):
        string_equality_validator = Equality(compare_with)
        return self._execute(string, string_equality_validator, none_exception)

    def empty(self, string):
        empty_string_validator = Empty()
        return self._execute(string, empty_string_validator, True)

    def available_date_string(self, item_to_validate, none_exception=True):
        available_date_string_validation = AvailableDateString()
        return self._execute(item_to_validate, available_date_string_validation, none_exception)

    def only_english(self, string, none_exception=True):
        only_english_validation = OnlyEnglish()
        return self._execute(string, only_english_validation, none_exception)

    def only_persian(self, string, none_exception=True):
        only_persian_validation = OnlyPersian()
        return self._execute(string, only_persian_validation, none_exception)

    def object_id(self, string, none_exception=True):
        object_id_validation = ObjectId()
        return self._execute(string, object_id_validation, none_exception)
