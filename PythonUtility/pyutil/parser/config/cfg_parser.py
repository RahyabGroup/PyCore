from configparser import ConfigParser

from pyutil.parser.config.section import Section

__author__ = 'H.Rouhani'


class CfgParser:
    _parser = None
    _file_path = None

    def __init__(self, file_path, encoding='utf-8'):
        self._file_path = file_path
        self._parser = ConfigParser(allow_no_value=True)
        self._parser.read(file_path, encoding=encoding)

    def section(self, sec_name):
        section = Section(sec_name, self)
        return section
