from pyutil.parser.config.option import Option

__author__ = 'H.Rouhani'


class Section:
    _section_name = None
    _cfg = None

    def __init__(self, section_name, cfg):
        self._section_name = section_name
        self._cfg = cfg

    def option(self, option_name):
        option = Option(option_name, self)
        return option
