import os

from pyutil.parser.config.cfg_parser import CfgParser

__author__ = 'H.Rouhani'


class SingletonConfig:
    instance = None
    _parser = None
    _user_defined_section_name = None

    def __new__(cls, *args, **kwargs):
        if SingletonConfig.instance is None:
            SingletonConfig.instance = super(SingletonConfig, cls).__new__(cls, *args, **kwargs)
        return SingletonConfig.instance

    def __init__(self, config_mode_key, cfg_file_directory, default_cfg_file_name='dev.cfg', user_defined_section_name='user_conf'):
        self._user_defined_section_name = user_defined_section_name
        app_mode = os.environ.get(config_mode_key, None)
        cfg_file_name = '{}.cfg'.format(app_mode) if app_mode else default_cfg_file_name
        cfg_file_path = '{}{}{}'.format(cfg_file_directory, os.sep, cfg_file_name)
        self._parser = CfgParser(cfg_file_path)

    def __getitem__(self, item):
        self._parser.section(self._user_defined_section_name).option(item).string_get()

    def __setitem__(self, item, value):
        self._parser.section(self._user_defined_section_name).option(item).set(value)
