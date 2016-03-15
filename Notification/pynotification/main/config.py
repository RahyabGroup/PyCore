import os
import logging

from pyfacil.config.singleton_config import SingletonConfig

__author__ = 'H.Rouhani'


class Config(SingletonConfig):
    def __init__(self):
        super().__init__('NOTIFICATION_CFG_MODE', os.path.dirname(__file__))

    @property
    def mongo_connection(self):
        return self._parser.section('mongodb_conf').option('connection_string').string_get()

    @property
    def mongo_db_name(self):
        return self._parser.section('mongodb_conf').option('db_name').string_get()

    @property
    def secret_key(self):
        return self._parser.section('app_conf').option('secret_key').string_get()

    @property
    def security_url(self):
        return self._parser.section('app_conf').option('security_url').string_get()

    @property
    def log_path(self):
        return self._parser.section('app_conf').option('log_path').string_get()

    @property
    def log_level(self):
        level = self._parser.section('app_conf').option('log_level').string_get()
        level = logging._nameToLevel.get(level, logging.DEBUG)
        return level
